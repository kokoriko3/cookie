# チャットアプリ

## 概要：

ルーム名を入力するだけで複数人とチャットができるアプリです

## 使用技術:

**バックエンド**:`Python 3.13,Django 4.2, Channels

**フロントエンド**:HTML5, Vanilla JavaScript (WebSocket API)

**データベース:**PosgreSQL

**インフラ・環境**: Docker, Docker Compose, AWS EC2 (Ubuntu)

## EC2へのデプロイ

### 1:AWS EC2(ubuntu)インスタンスを立ち上げポート80(HTTP)を開放します

### 2:EC2サーバー内でd git と docker 、docker-compose-v2をインストール

sudo apt-get update

sudo apt install -y git docker.io docker-compose-v2

sudo systemctl start docker
sudo systemctl enable docker

### 3:リポジトリのクローン

git clone https://github.com/kokoriko3/cookie

cd cookie

### 4:.envの作成

nano .env

.envに以下を記述

DEBUG=False

DJANGO_ALLOWED_HOSTS=*
DJANGO_SECRET_KEY=your-production-secret-key
DJANGO_LOGLEVEL=info

DATABASE_ENGINE=postgresql_psycopg2
DATABASE_NAME=dockerdjango
DATABASE_USERNAME=dbuser
DATABASE_PASSWORD=your_secure_password
DATABASE_HOST=db
DATABASE_PORT=5432

### 5:コンテナの起動とデータベース構築

sudo docker compose up -d --build

sudo docker compose run --rm django-web python manage.py migrate

sudo docker compose run --rm django-web python manage.py createsuperuser


# 工夫点

リアルタイムに動作するらしい


# 苦労点

デプロイ後のデータベースの構築に苦戦し
