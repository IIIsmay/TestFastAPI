# TestFastAPI
## Стек
- Python 3.14
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker / Docker Compose

## Возможности
- Создание чатов
- Отправка сообщений в чат
- Получение сообщений с лимитом
- Удаление чата с каскадным удалением сообщений

## Запуск

1. Клонировать репозиторий:
git clone https://github.com/IIIsmay/TestFastAPI.git

## Создать файл окружения:

copy .env.example .env

## Запустить проект:

docker compose up --build

## Документация Swagger:

http://localhost:8000/docs

## Тесты:

docker compose exec api pytest


