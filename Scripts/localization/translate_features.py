# -*- coding: utf-8 -*-
"""Translate Features.json user-facing strings to Simplified Chinese."""
import json
from pathlib import Path

FEATURES_PATH = Path(__file__).resolve().parents[2] / "Config" / "Features.json"

CAT = {
    "Privacy & Suggested Content": "隐私与推荐内容",
    "System": "系统",
    "Start Menu & Search": "开始菜单与搜索",
    "AI": "AI",
    "Windows Update": "Windows 更新",
    "Taskbar": "任务栏",
    "Appearance": "外观",
    "File Explorer": "文件资源管理器",
    "Gaming": "游戏",
    "Multi-tasking": "多任务",
    "Optional Windows Features": "可选 Windows 功能",
    "Other": "其他",
}

TRANSLATIONS = {
    # UiGroups labels
    "Taskbar search style": "任务栏搜索样式",
    "This setting allows you to customize the appearance of the search box on the taskbar.": "此设置允许您自定义任务栏上搜索框的外观。",
    "Show search box (Default)": "显示搜索框（默认）",
    "Show search icon and label": "显示搜索图标和标签",
    "Show search icon only": "仅显示搜索图标",
    "Hide": "隐藏",
    "Show taskbar apps on": "在以下位置显示任务栏应用",
    "This setting allows you to choose where taskbar app buttons are shown when using multiple monitors.": "此设置允许您选择使用多个显示器时任务栏应用按钮的显示位置。",
    "All taskbars (Default)": "所有任务栏（默认）",
    "Main taskbar and taskbar where window is open": "主任务栏和窗口所在任务栏",
    "Taskbar where window is open": "窗口所在任务栏",
    "Combine taskbar buttons on the main display": "合并主显示器上的任务栏按钮",
    "This setting allows you to choose how taskbar buttons are combined on the main display.": "此设置允许您选择主显示器上任务栏按钮的合并方式。",
    "Always (Default)": "始终（默认）",
    "When taskbar is full": "任务栏已满时",
    "Never": "从不",
    "Combine taskbar buttons on secondary displays": "合并副显示器上的任务栏按钮",
    "This setting allows you to choose how taskbar buttons are combined on secondary displays.": "此设置允许您选择副显示器上任务栏按钮的合并方式。",
    "Remove pinned apps from the start menu": "从开始菜单移除固定应用",
    "This setting allows you to quickly remove all pinned apps from the start menu.": "此设置允许您快速从开始菜单移除所有固定应用。",
    "Remove for the selected user": "为所选用户移除",
    "Remove for all users": "为所有用户移除",
    "Open File Explorer to": "文件资源管理器打开位置",
    "This setting allows you to choose the default location that File Explorer opens to.": "此设置允许您选择文件资源管理器默认打开的位置。",
    "Home (Default)": "主页（默认）",
    "This PC": "此电脑",
    "Downloads": "下载",
    "OneDrive": "OneDrive",
    "Drive letter position": "驱动器号位置",
    "This setting allows you to choose where drive letters are shown in File Explorer.": "此设置允许您选择驱动器号在文件资源管理器中的显示位置。",
    "Show drive letters after drive label (Default)": "在驱动器标签后显示驱动器号（默认）",
    "Show drive letters before drive label": "在驱动器标签前显示驱动器号",
    "Show network drive letters before drive label": "在网络驱动器标签前显示驱动器号",
    "Hide all drive letters": "隐藏所有驱动器号",
    "Show tabs from apps when snapping or pressing Alt+Tab": "贴靠窗口或按 Alt+Tab 时显示应用标签页",
    "This setting allows you to choose whether to show tabs from apps (such as Edge browser tabs) when snapping windows or pressing Alt+Tab.": "此设置允许您选择在贴靠窗口或按 Alt+Tab 时是否显示应用标签页（如 Edge 浏览器标签页）。",
    "Don't show tabs": "不显示标签页",
    "Show 3 most recent tabs (Default)": "显示最近 3 个标签页（默认）",
    "Show 5 most recent tabs": "显示最近 5 个标签页",
    "Show 20 most recent tabs": "显示最近 20 个标签页",
    "Start menu 'All Apps' view": "开始菜单「所有应用」视图",
    "This setting allows you to change the layout of the 'All Apps' section in the start menu, or hide it entirely. Hiding this section may make it harder to find installed apps on your system. This feature uses policies, which will lock down certain settings.": "此设置允许您更改开始菜单中「所有应用」部分的布局，或完全隐藏它。隐藏此部分可能会使查找已安装应用更加困难。此功能使用策略，将锁定某些设置。",
    "Category (Default)": "分类（默认）",
    "Grid": "网格",
    "List": "列表",
}

def tr(s):
    if not s:
        return s
    if s in CAT:
        return CAT[s]
    return TRANSLATIONS.get(s, s)

def main():
    data = json.loads(FEATURES_PATH.read_text(encoding="utf-8"))

    for c in data["Categories"]:
        c["Name"] = tr(c["Name"])

    for g in data["UiGroups"]:
        if g.get("Category"):
            g["Category"] = tr(g["Category"])
        if g.get("Label"):
            g["Label"] = tr(g["Label"])
        if g.get("ToolTip"):
            g["ToolTip"] = tr(g["ToolTip"])
        for v in g.get("Values", []):
            if v.get("Label"):
                v["Label"] = tr(v["Label"])

    for feat in data["Features"]:
        if feat.get("Category"):
            feat["Category"] = tr(feat["Category"])
        for key in ("Label", "ToolTip", "ApplyText", "UndoLabel", "ApplyUndoText"):
            if feat.get(key):
                feat[key] = tr(feat[key])

    FEATURES_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Written {FEATURES_PATH}")

if __name__ == "__main__":
    main()
