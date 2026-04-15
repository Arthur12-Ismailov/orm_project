Backend API для блога с использованием FastAPI и SQLAlchemy ORM

- User (пользователь)
- Profile (профиль)
- Post (пост)
- Tag (тег)

- One-to-One: User → Profile
- One-to-Many: User → Post
- Many-to-Many: Post ↔ Tag

- CRUD операции для пользователей
- Поиск по ID
- Получение постов пользователя
- Фильтрация по тегам

pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload

python demo.py