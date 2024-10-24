# AMD-AutoPowerEfficiencyTest

## Introduction || 介绍
copyright[@LingYuWings](https://github.com/LingYuWings) || [FunTech](https://space.bilibili.com/9321359)

This script is developed for automatic test of AMD CPU's power efficiency. The script developed using python, need outer tools ryzenadj and Cinebench R23 to run the test. 
The published tool is for Windows only, it uses powershell script to run the Cinebench test and collect the data used to draw the graph of the data(output as png and svg files and saved in the graph folder).

这个脚本是用于自动化进行AMD的能耗曲线测试，使用Python开发，需要ryzenadj和Cinebench R23用于运行自动化测试，发布包中不提供这两个工具。
发布的工具仅限于Windows中使用，脚本会使用powershell自动运行Cinebench测试并使用得到的结果绘制曲线和折线图，以svg和png格式输出至graph文件夹。

## How to use || 使用说明

### 1. Environment preparation || 环境准备

#### (1)Download tools || 工具下载

You can find RyzenAdj in [RyzenAdj-FlyGoat](https://github.com/FlyGoat/RyzenAdj), download newest version.

Cinebench R23 can be found at the floowing link [Cinebench R23 Download](https://www.techspot.com/downloads/7579-cinebench-r23.html)

Once you download these tools, put them inside the folder as followed tree:

AMDAutoPET_Ver2<p>
├─CinebenchR23<p>
├─graph<p>
└─ryzenadj

#### (2)Environment setting || 运行环境设置

Then open the powershell to set the running environment using folloing command:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

Then run the script, the test will run automaticlly.
