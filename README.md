# 박광우의 Claude Code 거버넌스 자료 → Codex 이식 키트

소망교회 청년교구 형, 안녕! 박광우 친구가 보낸 AI 비서 셋업 키트야.

이거 ZIP 풀고 아래 한 줄 명령 던지면 형 환경에 맞게 알아서 깔아줘.

---

## 형의 환경 가정

- **ChatGPT Plus** 구독자 ($20/월)
- Windows PC
- 코딩 처음 또는 가끔

---

## 사전 준비 (한 번만, 약 5분)

### 1. Codex CLI 설치

PowerShell을 **관리자 권한**으로 열고:

```powershell
npm install -g @openai/codex
```

(npm이 없으면 [Node.js](https://nodejs.org) 먼저 설치)

### 2. ChatGPT 로그인

```powershell
codex login
```

→ 브라우저 자동 열림 → ChatGPT 계정 로그인 → 끝.

---

## 본 작업 (Codex가 알아서 함)

### 3. 이 폴더로 이동

```powershell
cd C:\Users\<형이름>\Desktop\박광우_거버넌스_for_친구
```

### 4. Codex 켜기

```powershell
codex
```

### 5. 아래 명령 한 줄 복붙

```
이 폴더는 박광우 친구의 Claude Code 거버넌스 자료야. 내 Codex CLI 환경에
맞춰 변환해서 설치해줘.

요구사항:
- 푸른초장요양원 도메인 전용 정책(케어포·평가매뉴얼)은 빼고, 일반 운영
  원칙(알렉스 7원칙·문서화·MCP 구성·에이전트 병렬·백업·비밀처리·슬래시
  커맨드)만 가져와.
- CLAUDE.md → AGENTS.md 이름 변환.
- ~/.claude/settings.json 의 훅·권한 설정은 Codex 의 config.toml 형식
  으로 변환해서 ~/.codex/config.toml 에 배치.
- 박광우님 절대 경로(D:\메인작업·C:\Users\user 등)는 내 환경 경로로
  치환.
- 푸른초장요양원 도메인 정책 자리는 빈 채로 두고, "소망교회 청년교구
  도메인 정책 — 추후 채울 자리" placeholder 만 남겨줘.
- 변경된 파일 목록과 확인 절차를 마지막에 출력해.

Codex 공식 문서 https://developers.openai.com/codex/ 를 먼저 참고해서
정확한 위치·문법으로 작업해줘.
```

→ Codex 가 알아서: 공식 문서 검색 → plan 수립 → 파일 변환·이식 → 결과
보고.

---

## 검증 (Codex 작업 끝나면)

```
알렉스 7원칙 알고 있어? 어디서 봤어?
```

→ 7개 다 답하고 출처로 형 환경의 AGENTS.md 가리키면 성공.

---

## 폴더 안에 뭐가 있나

```
박광우_거버넌스_for_친구\
  ├── README.md                     ← 이 파일
  ├── global\
  │   ├── CLAUDE.md                 ← Claude 글로벌 (참조: ~/.claude/CLAUDE.md)
  │   └── settings.json             ← 훅·권한·statusLine 설정 참조용
  └── governance\
      ├── CLAUDE.md                 ← 거버넌스 마스터 (D:\메인작업\CLAUDE.md)
      ├── policies\                 ← 정책 8종 (알렉스-7원칙 포함)
      ├── hooks\                    ← 차단 훅·statusline 스크립트
      ├── agents\                   ← 도메인 3 + 엔지니어급 5 에이전트
      ├── playbooks\                ← 표준 운영 절차 6종
      └── tools\                    ← 공통 도구 (notify.py 등)
```

Codex 가 위 자료 전부 읽고 형 환경에 맞게 변환·이식해.

---

## 안 되는 거 있으면

화면 캡쳐 박광우 친구에게 카톡. 같이 봐줄게.

---

## ChatGPT Plus 사용량 안내

Plus 는 Codex CLI 사용량 한도가 Pro 보다 낮아. 무거운 자율 에이전트
작업(코드 대량 리팩토링·테스트 자동 실행 등)을 매일 돌리면 한도 도달
가능. 일반 사역 문서 보조·설교 준비·새가족 관리 정도는 충분히 여유 있어.

한도 부족 느껴지면 그때 Pro 로 업그레이드 고려.

---

## 박광우의 한 줄

> "내가 1년간 다듬은 자동화 거버넌스야. 형이 Codex 로 청년사역 자동화
> 만드는 출발선으로 써. 내 푸른초장 도메인은 빠지고 골격만 가니까, 형
> 도메인(설교·셀·새가족·심방·행사 등)을 차근차근 채워가면 돼."
