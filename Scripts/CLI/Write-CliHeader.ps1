# Prints the header for the script
function Write-CliHeader {
    param (
        $title
    )

    $fullTitle = " Win11Debloat 脚本 - $title"

    if ($script:Params.ContainsKey("Sysprep")) {
        $fullTitle = "$fullTitle（Sysprep 模式）"
    }
    else {
        $fullTitle = "$fullTitle (User: $(Get-UserName))"
    }

    Clear-Host
    Write-Host "-------------------------------------------------------------------------------------------"
    Write-Host $fullTitle
    Write-Host "-------------------------------------------------------------------------------------------"
}
