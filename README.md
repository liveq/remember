# 부고장 (Obituary Notice)

고급스러운 Dior 톤의 온라인 부고장 웹페이지입니다.

## 주요 기능

- **반응형 디자인**: 모바일, 태블릿, 데스크톱 모두 최적화
- **화이트/골드 톤**: 정갈하고 품격있는 Dior 스타일 디자인
- **계좌정보 모달**: 상주 이름 클릭 시 계좌정보 표시 및 복사 기능
- **6남매 + 배우자**: 공간을 넉넉하게 배분한 가족 정보 영역

## 정보 수정 방법

`index.html` 파일을 열어 다음 정보를 수정하세요:

### 1. 고인 정보 (52-59번 줄)
```html
<div class="deceased-name">故 홍길동</div>
<div class="deceased-dates">1950. 01. 01 - 2025. 10. 28</div>
```

### 2. 장례식장 정보 (66-86번 줄)
```html
<div class="info-value">2025년 10월 30일 오전 9시</div>
<div class="info-value">서울대학교병원 장례식장</div>
<div class="info-value">특1호실</div>
<div class="info-value">서울특별시 종로구 대학로 101</div>
<div class="info-value">02-1234-5678</div>
```

### 3. 배우자 정보 (96-101번 줄)
```html
<div class="family-member" onclick="showAccountModal('김영희', '부인', '국민은행', '123-456-789012')">
    <div class="family-member-name">김영희</div>
    <div class="family-member-relation">부인</div>
</div>
```

### 4. 자녀 정보 (107-142번 줄)
각 자녀의 이름, 관계, 은행, 계좌번호를 수정하세요:
```html
<div class="family-member" onclick="showAccountModal('홍철수', '장남', '신한은행', '110-234-567890')">
```

### 5. 고인 사진 추가 (선택사항)
사진을 추가하려면 52번 줄의 `<div class="photo-placeholder">`를 다음과 같이 변경:
```html
<img src="photo.jpg" alt="고인 사진" style="width: 180px; height: 240px; object-fit: cover; border: 3px solid #d4af37; border-radius: 2px;">
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
