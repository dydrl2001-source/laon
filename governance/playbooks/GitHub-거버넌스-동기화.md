# 플레이북: GitHub 거버넌스 동기화

`https://github.com/pkw4260-coder/automation-governance` 비공개 repo의 일상적 운용·새 PC 복원·인증 갱신.

## 일상 운용 (변경 → commit → push)

```powershell
cd D:\메인작업
git status                            # 변경 사항 확인
git diff                              # 상세 보기
git add <변경된 파일들>                # 또는 git add -A (단, .env 같은 secret 검토 후)
git commit -m "<type>: <변경 요약>"
git push
```

커밋 메시지 prefix:
- `feat:` 새 정책·스킬·에이전트·플레이북
- `fix:` 잘못된 정보 수정
- `docs:` 설명 보완·README
- `chore:` .gitignore·도구 설정
- `refactor:` 구조 변경 (의미는 동일)

## 새 PC 복원 (시나리오: 메인 PC 망가짐)

### 1. 사전 준비

새 PC에:
- Git 설치
- gh CLI 설치 (`winget install GitHub.cli`)
- Python 3.x 설치 (manifest 동기화 도구용)
- Claude Code 설치 + 로그인

### 2. 거버넌스 repo clone

```powershell
mkdir D:\
cd D:\
git clone https://github.com/pkw4260-coder/automation-governance.git 메인작업
```

### 3. gh 인증

```powershell
gh auth login
```

### 4. 글로벌 CLAUDE.md import 라인 추가

```powershell
Add-Content $env:USERPROFILE\.claude\CLAUDE.md "@D:\메인작업\CLAUDE.md"
```

### 5. 자동화 프로젝트별 폴더 복원

각 프로젝트는 별도 백업본에서 복원 (예: 매월 1일 ZIP). 거버넌스 repo는 정책·스킬·에이전트·플레이북만 들고 있고 실제 자동화 코드는 별도.

### 6. .env 파일 별도 복원

`.gitignore`에서 제외돼 있으므로 별도 안전 저장소(KeePass·암호 매니저)에서 복원.

### 7. 검증

```powershell
cd D:\메인작업
git log --oneline | head -10           # 최근 커밋 정상 표시
```

새 Claude Code 세션 시작 후:
- "백업 정책이 뭐야?" 질문 → 거버넌스 정책 답하면 자동 상속 OK

## gh 인증 갱신

토큰 만료 시:
```powershell
gh auth refresh
```

또는 재로그인:
```powershell
gh auth logout
gh auth login
```

## 비공개 / 공개 전환

비공개 → 공개 전 반드시:
- [ ] 모든 .env / credentials / 토큰 파일 미추적 확인
- [ ] git history에 비밀 정보 없는지 검토 (`git log -p | grep -i "password\|secret\|token"`)
- [ ] 어르신 개인정보 (이름·주민번호) 본문에 없는지 확인
- [ ] 결정: 공개 시 → 푸른초장요양원 도메인 노하우 외부 공개 의미

권장: **영구 비공개 유지** (개인정보 + 도메인 자산).

## 트러블슈팅

| 증상 | 원인 | 조치 |
|---|---|---|
| `git push` 거부됨 (rejected) | 원격이 더 앞섬 | `git pull --rebase` 후 재시도 |
| gh 인증 실패 | 토큰 만료 | `gh auth refresh` |
| 한글 파일명 octal escape 표시 | git 기본값 | `git config --global core.quotepath false` |
| `Updates were rejected because the tip of your current branch is behind` | 원격 변경 미반영 | `git pull --rebase` |

## 관련 자료

- 정책: `policies/비밀처리.md`, `policies/문서화.md`
- README: `D:\메인작업\README.md` (새 PC 빠른 시작)
