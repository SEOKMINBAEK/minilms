# Django 데모 프로젝트 실행 가이드

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
