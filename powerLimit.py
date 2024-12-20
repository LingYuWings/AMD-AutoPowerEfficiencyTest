import subprocess
import time
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_svg

# 获取当前的工作目录
current_directory = os.getcwd()

# 设置当前目录为工作目录
os.chdir(current_directory)

def set_power_limit(power_limit_w):
    power_limit_mw = power_limit_w * 1000
    ryzenadj_path = r'.\ryzenadj\ryzenadj.exe'
    ryzenadj_command = f'"{ryzenadj_path}" --stapm-limit={power_limit_mw} --fast-limit={power_limit_mw} --slow-limit={power_limit_mw}'
    subprocess.run(ryzenadj_command, shell=True)

def run_r23_benchmark():
    powershell_script = r'''
    Remove-Item -Path 'test.txt' -ErrorAction SilentlyContinue
    Remove-Item -Path 'result.csv' -ErrorAction SilentlyContinue

    $cinebenchPath = '.\CinebenchR23\Cinebench.exe'

    & $cinebenchPath -g_CinebenchCpuXTest=true | findstr CB >> test.txt

    $content = Get-Content 'test.txt'
    $modifiedContent = $content -replace 'CB ', '' -replace ' \(0.00\)', ''
    $modifiedContent | Out-File 'result.csv' -Encoding UTF8
    '''
    # 使用绝对路径的 PowerShell 来执行脚本
    powershell_path = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
    
    subprocess.run([powershell_path, "-Command", powershell_script], check=True)

def read_r23_score():
    try:
        with open('result.csv', 'r', encoding='utf-8-sig') as f:
            line = f.readline().strip()
            score = float(line)
            return score
    except (ValueError, FileNotFoundError) as e:
        print(f'Can\'t get benchmark score: {e}')
        return None

def plot_graphs(csv_file):
    """
    根据CSV文件绘制拟合曲线和未拟合的折线图，保存为SVG和PNG格式。
    """
    # 读取数据
    data = pd.read_csv(csv_file)
    x = data['Power Limit(W)']
    y = data['Cinebench R23 Score']

    # 设置图形大小和样式
    fig, ax = plt.subplots(figsize=(16, 9))

    # 1. 绘制原始折线图
    ax.plot(x, y, marker='o', color='blue')
    ax.set_xlabel('Power Limit(W)', color='white')
    ax.set_ylabel('R23 Score', color='white')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.legend()

    # 设置背景透明
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)

    # 保存折线图为SVG和PNG格式
    plt.savefig('./graph/line_chart.svg', format='svg', transparent=True, bbox_inches='tight', dpi=300)
    plt.savefig('./graph/line_chart.png', format='png', transparent=True, bbox_inches='tight', dpi=300)

    # 清空图形以重新绘制
    ax.clear()

    # 2. 绘制拟合曲线
    z = np.polyfit(x, y, 3)  # 3阶多项式拟合
    p = np.poly1d(z)
    x_fine = np.linspace(min(x), max(x), 500)
    y_fitted = p(x_fine)

    # 绘制拟合曲线
    ax.plot(x_fine, y_fitted,  color='red')
    ax.set_xlabel('Power Limit(W)', color='white')
    ax.set_ylabel('R23 Score', color='white')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.legend()

    # 保存拟合曲线为SVG和PNG格式
    plt.savefig('./graph/fitted_curve.svg', format='svg', transparent=True, bbox_inches='tight', dpi=300)
    plt.savefig('./graph/fitted_curve.png', format='png', transparent=True, bbox_inches='tight', dpi=300)

    # 关闭图形，释放内存
    plt.close()

# 添加 CSV 文件标题
with open('overall_results.csv', 'w', encoding='utf-8') as f:
    f.write('PowerLimit(W),Cinebench R23 Score\n')

lang= input("Please choose the language||请选择语言：\nEnglish(E)||中文(C) please enter:")

if lang == "e" or lang == "E":
    power_low=input("Please enter the minimun power of the test(W):")
    power_high=input("Please enter the highest power of the test(W):")
    between_p=input("Please enter the gap bewteen two tests(W):")
elif lang == "c" or lang == "C":
    power_low=input("请输入测试功耗最小值(W):")
    power_high=input("请输入测试功耗最大值(W):")
    between_p=input("请输入两次测试间隔的功耗大小(W):")

# 主测试循环
for power_limit in range(power_low, power_high, between_p):
    print(f'Setting power limit to {power_limit}W')
    set_power_limit(power_limit)
    time.sleep(5)  # 等待功耗限制生效

    print('Start running Cinebench R23 benchmark')
    run_r23_benchmark()

    score = read_r23_score()
    print(f'R23 score: {score}')

    # 记录结果到文件
    with open('overall_results.csv', 'a', encoding='utf-8') as f:
        f.write(f'{power_limit},{score}\n')

    # 等待一段时间，防止系统过热
    time.sleep(60)

# 运行完所有测试后，生成图像
plot_graphs('overall_results.csv')
