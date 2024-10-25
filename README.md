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

Once you download these tools, put them inside the folder as followed tree folder structure:

    AMDAutoPET
    ├─CinebenchR23
    ├─graph
    └─ryzenadj

你可以在RyzenAdj项目[RyzenAdj-FlyGoat](https://github.com/FlyGoat/RyzenAdj)下载到最新版本的RyzenAdj，在这个站点[Cinebench R23 Download](https://www.techspot.com/downloads/7579-cinebench-r23.html)找到Cinebench R23的下载。

下载完成后，请将文件放置在以下目录结构中：

    AMDAutoPET
    ├─CinebenchR23
    ├─graph
    └─ryzenadj

#### (2)Environment setting || 运行环境设置

Then open the powershell to set the running environment using folloing command:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

Then run the script using administrator permission, the test will run automaticlly.

首先使用powershell运行以下命令：

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

之后使用管理员权限运行脚本的exe文件，测试会自动进行。

## Attention || 注意事项

This script's first version can only use to measure the power efficiency in range 15W to 65w. After the test, you may need to reboot your device or using ryzenadj to reset your CPU's power limit to normal setting.

这个脚本的首个版本仅用于测试15w-65w的能耗曲线，在测试结束后，你可能需要重启电脑或者使用ryzenadj来让你的功耗控制恢复至默认设置。