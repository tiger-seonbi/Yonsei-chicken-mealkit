# 파이썬 3.11 기반 이미지 사용
FROM python:3.11-slim

# 환경변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리 설정
WORKDIR /app

# 프로젝트의 requirements.txt를 컨테이너에 복사
COPY requirements.txt /app/requirements.txt

# requirements.txt에 명시된 패키지 설치
RUN pip install --upgrade pip && pip install -r requirements.txt

# 프로젝트 코드를 컨테이너에 복사
COPY . /app/

# 실행할 명령어 설정
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]