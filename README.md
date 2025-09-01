# URL
[[보러가기](minilms-production.up.railway.app)](https://minilms-production.up.railway.app/)

- ID: admin
- PW: 0000

최초 방문시 로그인 페이지가 나타나지 않는다면, /login으로 접속 부탁드립니다.

RAILWAY 환경 상 SMTP 메일 서버의 부재로 메일발송 테스트는 리포지토리 다운로드 후 로컬 환경에서 테스트 해주시면 감사하겠습니다.

로컬에서 실행할 시 main 브랜치로 실행해주세요.

model은 총 3가지로 구성되었습니다.

- Subject: 수업정보
- Curriculum: 교시정보(Subject 참조)
- Apply: 신청내역

신청내역 페이지를 제외한 페이지들은 fbv 방식으로 구현, 신청내역 페이지는 drf + Ajax로 CRUD를 구현하였습니다.

또한 수업신청 시 django.core.mail 모듈을 사용하여 확정메일이 발송되도록 구현하였습니다.(확인용 도메인에서는 SMTP 서버 구성을 못하였습니다)

화면의 경우 신청내역의 표를 제외한 대부분의 구성요소를 반응형으로 설계하여 모바일 및 태플릿 등과 대응될 수 있도록 하였습니다.

또한 사용자 입력폼들의 경우 입력 누락을 방지하기 위해 입력폼의 발생 이벤트에 맞춰 인터렉션하게 저장버튼의 활성화 여부를 검사합니다.

AI 코딩 보조 툴은 Github Copilot과 Claude를 활용하였습니다.

주 사용은, Django 프로젝트 설정(setting.py 초기 구성 등)

보일러플레이트 코드 생성(뷰 템플릿 및 폼 클래스 기본 구조)

마크업 및 와이어프레임(템플릿 및 레이아웃 & 반응형) 등의 틀을 잡을 때 활용하였습니다.

사용이유는

1. 시간 효율성: 반복적인 기본 설정 작업을 빠르게 처리
2. 일관성: 표준화된 코드 구조 유지
3. 학습 도구: 새로운 패턴이나 설정 사용법 참고

하지만 세밀한 로직 및 커스터마이징은 직접 작업하였으며 생성된 코드의 검토와 최적화를 진행했습니다.

전반적으로 기초 작업의 생산성 향상에 큰 도움이 되었습니다.

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
