# 플레이북: C 디스크 압박 해소 절차

C: 드라이브 여유 공간이 위험 수준(< 10GB)에 들어왔을 때 즉시 실행.

## 트리거

- `Get-PSDrive C` 결과 Free < 10GB
- Claude Code temp 파일 ENOSPC 에러
- "디스크 풀" 또는 "공간 부족" 경고 팝업

## 즉시 점검 (1분)

```powershell
$c = Get-PSDrive C
"C: 여유 {0:N1} GB / 사용 {1:N1} GB / 총 {2:N1} GB" -f ($c.Free/1GB), ($c.Used/1GB), ($c.Used/1GB + $c.Free/1GB)
```

## 우선순위별 회복 절차

### 1순위: 백업 도구 잔여물 (즉시 4-5GB 회복 가능)

```powershell
# 이전 영상편집 미러 잔존 (4.9GB)
Test-Path "C:\Users\user\백업도구\결과\_mirror"  # 있다면
Remove-Item "C:\Users\user\백업도구\결과\_mirror" -Recurse -Force
```

### 2순위: 디스크 정리 마법사

```powershell
cleanmgr.exe /sageset:1     # 한 번만 (옵션 저장)
cleanmgr.exe /sagerun:1     # 실행
```

또는 GUI:
- 시작 → "디스크 정리" 검색 → C: 선택 → "시스템 파일 정리" 클릭

체크 권장:
- Windows Update 정리 (수GB 회복 가능)
- 임시 파일
- 다운로드한 프로그램 파일
- 휴지통

### 3순위: 다운로드 폴더 정리

```powershell
Get-ChildItem $env:USERPROFILE\Downloads -File | Sort-Object Length -Descending | Select-Object -First 20 Name, @{n="MB";e={[math]::Round($_.Length/1MB,1)}}
```

설치 끝낸 .exe / .msi 파일 우선 삭제.

### 4순위: 큰 폴더 진단

```powershell
Get-ChildItem C:\Users\user -Directory | ForEach-Object {
  $sz = (Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
  [PSCustomObject]@{ Name = $_.Name; GB = [math]::Round($sz/1GB,2) }
} | Sort-Object GB -Descending | Select-Object -First 15
```

GB 단위 폴더 발견 시 D 드라이브로 이전 검토 (사용자 결정 필수).

### 5순위: D 드라이브 이전

C에 있는 자동화 프로젝트 / 데이터를 D로 옮기는 경우 — `playbooks/신규-프로젝트-온보딩.md` 의 manifest 갱신 절차 따름.

이전 후 C에 빈 폴더 잔존하면 (CWD 락 가능성) Claude Code 종료 후 탐색기에서 직접 삭제.

## 영구 예방

`skills/풀-디스크-사고-회피.md` 정책 준수:
- 백업 결과물 D:\에만 저장 (`backup_projects.ps1` `$DestRoot = "D:\..."`)
- GB 단위 폴더는 미러링(증분), ZIP 금지
- 매월 1일 1회만 실행
- C 임시 경유 금지

## 사고 학습 (2026-05-07)

- 사건: C: 217GB 중 488MB 잔여
- 원인: backup_projects.ps1 결과를 C에 출력 + 영상편집 5GB 미러 + 평소 C 여유 ~10GB
- 복구: _mirror 삭제 → 사용자 정리 추가 → C 여유 8GB 복원
- 영구 조치: 모든 자동화 D 드라이브 이전 + 백업 출력 D 고정

## 관련 자료

- 스킬: `skills/풀-디스크-사고-회피.md`
- 정책: `policies/백업.md`
- 사고 로그: `D:\백업도구\결과\backup_log.txt` (2026-05-07 분)
