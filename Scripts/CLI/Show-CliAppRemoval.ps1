# Shows the CLI app removal menu and prompts the user to select which apps to remove.
function Show-CliAppRemoval {
    Write-CliHeader "卸载应用"

    Write-Output "> 正在打开应用选择窗口..."

    $result = Show-AppSelectionWindow

    if ($result -eq $true) {
        Write-Output "你已选择卸载 $($script:SelectedApps.Count) 个应用"
        Add-Parameter 'RemoveApps'
        Add-Parameter 'Apps' ($script:SelectedApps -join ',')

        Save-Settings

        # Suppress prompt if Silent parameter was passed
        if (-not $Silent) {
            Write-Output ""
            Write-Output ""
            Write-Output "按 Enter 卸载所选应用，或按 CTRL+C 退出..."
            Read-Host | Out-Null
            Write-CliHeader "卸载应用"
        }
    }
    else {
        Write-Host "选择已取消，未卸载任何应用" -ForegroundColor Red
        Write-Output ""
    }
}