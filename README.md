# 부고장 (Obituary Notice)

고급스러운 Dior 톤의 온라인 부고장 웹페이지입니다.

## 주요 기능

- **반응형 디자인**: 모바일, 태블릿, 데스크톱 모두 최적화
- **화이트/골드 톤**: 정갈하고 품격있는 Dior 스타일 디자인
- **계좌정보 모달**: 상주 이름 클릭 시 계좌정보 표시 및 복사 기능
- **6남매 + 배우자**: 공간을 넉넉하게 배분한 가족 정보 영역

## 현재 정보 (양식2)

### 고인 정보
- **故 고영곤** (향년 85세)
- 사진 및 생년월일 생략

### 장례식장 정보
- **조문기간**: 2025년 10월 29일 ~ 31일
- **발인일시**: 2025년 10월 31일
- **장례식장**: 은파장례문화원
- **빈소**: 2층 특실
- **주소**: 전북특별자치도 군산시 미성로 512

### 상주 정보
- 아들 고석우 / 며느리 소유진
- 딸 고현숙
- 딸 고은희 / 사위 김재구
- 딸 고현신 / 사위 최윤모
- 딸 고현준 / 사위 김신중
- 딸 고현경 / 사위 조상원

### 계좌 정보
- 현재: 추후 안내 예정
- 계좌 정보 업데이트 방법은 아래 참조

## 정보 수정 방법

`index.html` 파일을 열어 다음 정보를 수정하세요:

### 1. 고인 정보 (465-466번 줄)
```html
<div class="deceased-name">故 고영곤</div>
<div class="deceased-dates">향년 85세</div>
```

### 2. 장례식장 정보 (474-493번 줄)
```html
<div class="info-value">2025년 10월 29일 ~ 31일</div>
<div class="info-value">2025년 10월 31일</div>
<div class="info-value">은파장례문화원</div>
<div class="info-value">2층 특실</div>
<div class="info-value">전북특별자치도 군산시 미성로 512</div>
```

### 3. 상주 정보 및 계좌 정보 (505-559번 줄)
각 상주의 이름, 관계, 은행, 계좌번호를 수정하세요:
```html
<div class="family-member" onclick="showAccountModal('고석우', '아들', '신한은행', '110-234-567890')">
    <span class="account-hint"></span>
    <div class="family-member-name">고석우</div>
    <div class="family-member-relation">아들</div>
</div>
```

**계좌 정보 업데이트 시:**
- `'추후 안내'`를 실제 은행명으로 변경 (예: `'신한은행'`)
- `'추후 안내 예정'`을 실제 계좌번호로 변경 (예: `'110-234-567890'`)
- 복사 버튼이 자동으로 활성화됩니다

### 4. 고인 사진 추가 (선택사항)
현재는 사진이 숨겨져 있습니다. 사진을 추가하려면:
1. CSS에서 `.photo-placeholder { display: none; }`을 제거
2. HTML 465번 줄 전에 다음 코드 추가:
```html
<div class="photo-placeholder">
    <img src="photo.jpg" alt="고인 사진" style="width: 100%; height: 100%; object-fit: cover;">
</div>
```

## GitHub Pages 배포 설정

### 방법 1: GitHub 웹사이트에서 설정 (권장)

1. GitHub 리포지토리 페이지로 이동: https://github.com/liveq/remember
2. **Settings** 탭 클릭
3. 왼쪽 메뉴에서 **Pages** 클릭
4. **Source** 섹션에서:
   - Branch: `claude/session-011CUZrt2aThaoyNTb4U991A` 선택
   - Folder: `/ (root)` 선택
5. **Save** 버튼 클릭
6. 몇 분 후 페이지 상단에 접속 주소가 표시됩니다:
   - `https://liveq.github.io/remember/`

### 방법 2: main 브랜치로 병합 후 배포

main 브랜치 생성 권한이 있다면:

1. GitHub에서 Pull Request 생성
2. `claude/session-011CUZrt2aThaoyNTb4U991A` → `main` 병합
3. Settings → Pages에서 main 브랜치 선택

## 로컬에서 미리보기

브라우저에서 `index.html` 파일을 직접 열어 확인할 수 있습니다:

```bash
# 현재 디렉토리에서
open index.html  # macOS
xdg-open index.html  # Linux
start index.html  # Windows
```

또는 로컬 서버 실행:

```bash
# Python 3
python -m http.server 8000

# 브라우저에서 http://localhost:8000 접속
```

## 기술 스택

- HTML5
- CSS3 (그라데이션, 애니메이션, 반응형)
- Vanilla JavaScript (모달, 클립보드 API)
- Google Fonts (Noto Serif KR)

## 디자인 특징

- 유치한 이모티콘 없는 프로페셔널한 디자인
- 부드러운 그라데이션과 그림자 효과
- 고급스러운 골드 악센트
- 우아한 세리프 폰트
- 부드러운 hover 애니메이션
- 접근성을 고려한 색상 대비

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)
