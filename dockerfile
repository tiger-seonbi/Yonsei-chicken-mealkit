# 파이썬 3.11 기반 이미지 사용
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# requirements.txt 파일 복사
COPY requirements.txt /app/requirements.txt

# 의존성 설치
RUN pip install --upgrade pip && pip install -r requirements.txt

# 프로젝트 파일 복사
COPY . /app/

# media 디렉토리가 없으면 생성
RUN mkdir -p /app/media

# static 파일 수집
RUN python manage.py collectstatic --no-input

# Nginx 스테이지
FROM nginx:1.21

# Nginx 설정 복사
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Django static files 복사
COPY --from=builder /app/staticfiles /static

# Django media files 복사
COPY --from=builder /app/media /media
