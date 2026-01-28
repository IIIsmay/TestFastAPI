# TestFastAPI
## Стек
- Python 3.14
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker / Docker Compose

## Запуск

1. Клонировать репозиторий:
git clone https://github.com/IIIsmay/TestFastAPI.git

## Создать файл окружения:

copy .env.example .env

##Запустить проект:

docker compose up --build

##Тесты:

docker compose exec api pytest


