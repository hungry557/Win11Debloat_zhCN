# Win11Debloat

[![GitHub Release](https://img.shields.io/github/v/release/Raphire/Win11Debloat?style=for-the-badge&label=Latest%20release)](https://github.com/Raphire/Win11Debloat/releases/latest)
[![Join the Discussion](https://img.shields.io/badge/Join-the%20Discussion-2D9F2D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Raphire/Win11Debloat/discussions)
[![Static Badge](https://img.shields.io/badge/Documentation-_?style=for-the-badge&logo=bookstack&color=grey)](https://github.com/Raphire/Win11Debloat/wiki/)

Win11Debloat 是一款轻量、易用的 PowerShell 脚本，可让您快速精简和自定义 Windows 体验，无需安装！您可以用它移除预装应用、禁用遥测、去除侵入式界面元素等等。不必再逐个进入设置或一个个卸载应用，Win11Debloat 让这一切变得简单快捷。

脚本还包含许多系统管理员和高级用户会喜欢的功能，例如强大的命令行界面、对 Windows 审核模式的支持，以及为其他 Windows 用户应用更改的能力。您还可以方便地导出和导入偏好设置，在所有系统上快速应用相同配置。更多详情请参阅 [wiki](https://github.com/Raphire/Win11Debloat/wiki)。

![Win11Debloat Menu](/Assets/Images/menu.png)

#### 这个脚本对您有帮助吗？欢迎请我喝杯咖啡支持我的工作

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M5C6UPC)

## 使用方法

> [!Warning]
> 我们已尽力确保此脚本不会意外破坏系统功能，但请自行承担使用风险！如遇问题，请在此 [报告](https://github.com/Raphire/Win11Debloat/issues)。

### 快速方式

通过 PowerShell 自动下载并运行脚本。

1. 打开 PowerShell 或终端。
2. 将以下命令复制并粘贴到 PowerShell 中：

```PowerShell
& ([scriptblock]::Create((irm "https://debloat.raphi.re/")))
```

3. 等待脚本自动下载并启动 Win11Debloat。
4. 仔细阅读并按照屏幕上的说明操作。

此方式支持命令行参数以自定义脚本行为。更多信息请见[此处](https://github.com/Raphire/Win11Debloat/wiki/Command%E2%80%90line-Interface#parameters)。

### 传统方式

<details>
  <summary>手动下载并运行脚本。</summary><br/>

  1. [下载最新版脚本](https://github.com/Raphire/Win11Debloat/releases/latest)，并将 ZIP 文件解压到您想要的位置。
  2. 进入 Win11Debloat 文件夹
  3. 双击 `Run.bat` 文件启动脚本。注意：如果控制台窗口立即关闭且没有任何反应，请尝试下方的高级方式。
  4. 接受 Windows UAC 提示以管理员身份运行脚本，这是脚本正常运行所必需的。
  5. 仔细阅读并按照屏幕上的说明操作。
</details>

### 高级方式

<details>
  <summary>手动下载脚本并通过 PowerShell 运行。推荐给高级用户。</summary><br/>

  1. [下载最新版脚本](https://github.com/Raphire/Win11Debloat/releases/latest)，并将 ZIP 文件解压到您想要的位置。
  2. 以管理员身份打开 PowerShell 或终端。
  3. 通过输入以下命令临时启用 PowerShell 执行：

  ```PowerShell
  Set-ExecutionPolicy Unrestricted -Scope Process -Force
  ```

  4. 在 PowerShell 中，进入文件解压后的目录。例如：`cd c:\Win11Debloat`
  5. 输入以下命令运行脚本：

  ```PowerShell
  .\Win11Debloat.ps1
  ```

  6. 仔细阅读并按照屏幕上的说明操作。

  此方式支持命令行参数以自定义脚本行为。更多信息请见[此处](https://github.com/Raphire/Win11Debloat/wiki/Command%E2%80%90line-Interface#parameters)。
</details>

## 功能

以下是 Win11Debloat 主要功能的概览。更多详情请访问 [wiki](https://github.com/Raphire/Win11Debloat/wiki)。

> [!Tip]
> Win11Debloat 所做的几乎所有更改都可以轻松还原，几乎所有应用都可以通过 Microsoft Store 重新安装。有关还原更改的更多信息，请访问 [wiki](https://github.com/Raphire/Win11Debloat/wiki/Reverting-Changes)。

#### 应用移除

- 移除多种预装应用。更多信息请见[此处](https://github.com/Raphire/Win11Debloat/wiki/App-Removal)。

#### 隐私与推荐内容

- 禁用遥测、诊断数据、活动历史、应用启动跟踪和定向广告。
- 禁用 Windows、锁屏和 Microsoft Edge 中的提示、技巧、建议和广告。
- 禁用 Windows 定位服务、应用位置访问和查找我的设备位置跟踪。
- 隐藏设置「主页」页面上的 Microsoft 365 广告，或完全隐藏「主页」页面。

#### AI 功能

- 禁用并移除 Microsoft Copilot、Windows Recall 和 Click to Do。
- 防止 AI 服务（WSAIFabricSvc）自动启动。
- 禁用 Edge、画图和记事本中的 AI 功能。

#### 系统

- 禁用用于共享和移动文件的拖放托盘。
- 恢复旧版 Windows 10 风格右键菜单。
- 关闭增强指针精确度（鼠标加速）。
- 禁用粘滞键键盘快捷键。
- 禁用存储感知自动磁盘清理。
- 禁用快速启动以确保完全关机。
- 禁用 BitLocker 自动设备加密。
- 在 Modern Standby 期间禁用网络连接以减少电池消耗。

#### Windows 更新

- 防止 Windows 在更新可用后立即获取更新。
- 防止登录时更新后自动重启。
- 禁用与其他电脑共享已下载更新（即传递优化）。
- 防止 Windows 自动安装设备配套应用，如 LG Monitor App、Alienware Command Center 等。

#### 外观

- 为系统和应用启用深色模式。
- 禁用透明效果、动画和视觉效果。

#### 开始菜单和搜索

- 通过移除固定应用、隐藏推荐内容和自定义「所有应用」部分来自定义开始菜单。
- 禁用开始菜单中的手机连接移动设备集成。
- 在 Windows 搜索中禁用 Bing 网页搜索和 Copilot 集成以及 Microsoft Store 应用建议。

#### 任务栏

- 更改任务栏对齐方式。
- 自定义或隐藏搜索栏、任务视图等任务栏按钮。
- 禁用任务栏和锁屏上的小部件。
- 在任务栏右键菜单中启用「结束任务」选项以快速强制关闭应用。
- 在任务栏应用区域启用「上次活动点击」行为，允许您重复点击应用图标在该应用的打开窗口之间切换焦点。
- 自定义任务栏上应用按钮的显示方式。

#### 文件资源管理器

- 更改文件资源管理器默认打开位置。
- 显示已知文件类型的扩展名。
- 显示隐藏的文件、文件夹和驱动器。
- 从文件资源管理器导航窗格隐藏「主页」「图库」或 OneDrive 部分。
- 从文件资源管理器导航窗格隐藏重复的可移动驱动器条目，仅保留「此电脑」下的条目。
- 将常用文件夹（桌面、下载等）添加回文件资源管理器中的「此电脑」。
- 更改文件资源管理器中驱动器盘符的位置或可见性。

#### 多任务

- 禁用窗口贴靠。
- 拖动或贴靠窗口时禁用贴靠助手和贴靠布局建议。
- 更改贴靠窗口或按 Alt+Tab 时是否显示标签页。

#### 可选 Windows 功能

- 启用 Windows 沙盒，一个用于安全隔离运行应用程序的轻量级桌面环境。
- 启用适用于 Linux 的 Windows 子系统，允许您直接在 Windows 上运行 Linux 环境。

#### 其他

- 禁用 Xbox 游戏栏集成以及游戏/屏幕录制。卸载 Xbox 游戏栏后，这也会禁用 `ms-gamingoverlay`/`ms-gamebar` 弹窗。
- 禁用 Brave 浏览器中的冗余功能（AI、加密货币、新闻等）。

#### 高级功能

- 能够[将更改应用到其他用户](https://github.com/Raphire/Win11Debloat/wiki/Advanced-Features#running-as-another-user)，而非当前登录用户。
- [Sysprep 模式](https://github.com/Raphire/Win11Debloat/wiki/Advanced-Features#sysprep-mode)可将更改应用到 Windows 默认用户配置文件，确保所有新用户自动获得这些更改。

## 贡献

欢迎各类贡献！请参阅我们的[贡献指南](https://github.com/Raphire/Win11Debloat/blob/master/.github/CONTRIBUTING.md)了解如何开始及贡献最佳实践。

## 许可证

Win11Debloat 采用 MIT 许可证。更多信息请参阅 LICENSE 文件。
