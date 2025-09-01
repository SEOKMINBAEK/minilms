# URL
[[보러가기](minilms-production.up.railway.app)](https://minilms-production.up.railway.app/)

# 사이트맵

- /login: Django admin기능을 활용한 커스텀 로그인 페이지
- /subjects: 수업 app. root path로 들어오면 리다이렉트, index페이지는 수업소개 페이지입니다.
- /subjects/{:id}: 수업상세 페이지. 각 수업마다 설정된 커리큘럼(교시)를 표 형태로 보여주며, 활동사진을 업로드할 수 있습니다.
- /subjects/apply/{:id}: - 수업신청 페이지. 입력된 이메일로 확정 메일을 보내줍니다.
- /subjects/history: 수업신청내역을 확인, 추가, 수정, 삭제 CRUD 기능을 사용할 수 있습니다. 표에서 각 신청수업을 클릭하면 모달이 등장합니다.

# minilms 실행 가이드

## 1. 프로젝트 다운로드
```bash
git clone https://github.com/SEOKMINBAEK/minilms
```

## 2. 가상환경 생성
```bash
python -m venv venv

venv\Scripts\activate
```

## 3. 패키지 설치
```bash
pip install -r requirements.txt
```

## 4. 데이터베이스 설정
```bash
python manage.py migrate
```

## 5. 계정 생성(직접생성)
```bash
python manage.py create_superuser
```

## 6. 서버 실행
```bash
python manage.py runserver
```
