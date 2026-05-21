# Status line: [folder] [governance flag] | D drive free | carefor warning
$ErrorActionPreference = 'SilentlyContinue'

$payload = [Console]::In.ReadToEnd() | ConvertFrom-Json
$cwd = $payload.workspace.current_dir
if (-not $cwd) { $cwd = (Get-Location).Path }

$folder = Split-Path -Leaf $cwd

# D drive free space
$diskStr = "D:?"
try {
    $d = Get-PSDrive D -ErrorAction Stop
    $freeGB = [math]::Round($d.Free / 1GB, 1)
    $tag = if ($freeGB -lt 20) { " LOW!" }
           elseif ($freeGB -lt 50) { " warn" }
           else { "" }
    $diskStr = "D:${freeGB}GB$tag"
} catch { }

# Carefor 1관/2관 reminder
$careforHint = ""
if ($cwd -match 'carefor|케어포') {
    $careforHint = " | 1관/2관 facility 확인"
}

# Governance hub indicator (read-only meta-layer)
$hubHint = ""
if ($cwd -like '*메인작업*') {
    $hubHint = " [governance/RO]"
}

# Monthly backup verification reminder
# - From day 2 of each month onwards
# - Show only if D:\백업도구\결과\<YYYY-MM>_verified.txt is missing
$verifyHint = ""
$now = Get-Date
if ($now.Day -ge 2) {
    $sentinel = "D:\백업도구\결과\$($now.ToString('yyyy-MM'))_verified.txt"
    if (-not (Test-Path $sentinel)) {
        $verifyHint = " | !백업검증 필요(/백업확인)"
    }
}

Write-Output "[$folder]$hubHint | $diskStr$careforHint$verifyHint"
