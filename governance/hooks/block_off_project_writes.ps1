# PreToolUse hook: enforce 대칭 거버넌스 비침습 정책
#
# 동작 (2026-05-13 대칭 격리로 확장):
#   현재 CWD가 manifest.yaml의 projects[*].path 중 하나에 속하면,
#   "내 프로젝트 내부" 쓰기만 허용하고 다른 D:\ 경로 쓰기는 차단한다.
#
# 예:
#   CWD=D:\메인작업 → D:\메인작업\* 만 허용, 그 외 D:\* 차단
#   CWD=D:\주식     → D:\주식\* 만 허용, 그 외 D:\* 차단
#   CWD=D:\블로그자동화 → D:\블로그자동화\* 만 허용
#
# 비-D:\ 경로 (~/.claude 설정, C:\Users\... 등) 와 미등록 CWD 는 항상 통과한다.
# manifest.yaml 을 읽지 못하면 기존 "메인작업 단방향" 동작으로 폴백한다.

$ErrorActionPreference = 'Stop'

$payload = [Console]::In.ReadToEnd() | ConvertFrom-Json

$cwd = $payload.cwd
if (-not $cwd) { $cwd = (Get-Location).Path }

$fp = $payload.tool_input.file_path
if (-not $fp) { exit 0 }

$fpNorm  = ($fp  -replace '/', '\').TrimEnd('\')
$cwdNorm = ($cwd -replace '/', '\').TrimEnd('\')

# Non-D 경로는 항상 통과 (settings.json, ~/.claude 등)
if ($fpNorm -notlike 'D:\*') { exit 0 }

# manifest.yaml 에서 등록된 프로젝트 경로 목록 추출
$manifestPath = 'D:\메인작업\manifest.yaml'
$projectPaths = @()
try {
    # projects: 섹션 안의 'path: D:\xxx' 라인만 캡처
    $inProjects = $false
    foreach ($line in (Get-Content -LiteralPath $manifestPath -Encoding UTF8)) {
        if ($line -match '^projects:\s*$') { $inProjects = $true; continue }
        if ($inProjects -and $line -match '^\S' -and $line -notmatch '^projects:') {
            # 다음 최상위 키 등장 → projects 섹션 끝
            $inProjects = $false
        }
        if ($inProjects -and $line -match '^\s+path:\s*(.+?)\s*$') {
            $p = $matches[1].Trim().TrimEnd('\')
            if ($p -like 'D:\*') { $projectPaths += $p }
        }
    }
} catch {
    # manifest 못 읽으면 메인작업 단방향 폴백
    $projectPaths = @('D:\메인작업')
}

if ($projectPaths.Count -eq 0) {
    $projectPaths = @('D:\메인작업')
}

# CWD 가 어느 프로젝트에 속하는지 매칭
$cwdProject = $null
foreach ($p in $projectPaths) {
    if ($cwdNorm -eq $p -or $cwdNorm -like "$p\*") {
        $cwdProject = $p
        break
    }
}

# 미등록 CWD 는 제약 없음
if (-not $cwdProject) { exit 0 }

# 같은 프로젝트 내부 쓰기는 허용
if ($fpNorm -eq $cwdProject -or $fpNorm -like "$cwdProject\*") { exit 0 }

# 그 외 D:\ 경로 → 차단
$msg = "거버넌스 비침습 정책 차단: '$cwdProject' 세션에서는 다른 D 드라이브 경로 파일을 수정할 수 없습니다. 차단된 경로: $fpNorm. 해당 프로젝트 폴더에서 새 Claude Code 세션을 여세요."

$out = @{
    hookSpecificOutput = @{
        hookEventName = "PreToolUse"
        permissionDecision = "deny"
        permissionDecisionReason = $msg
    }
} | ConvertTo-Json -Compress

Write-Output $out
exit 0
