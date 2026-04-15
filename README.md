Простой backend на FastAPI с использованием ORM (SQLAlchemy)

- User (пользователь)
- Post (пост)

- Один ко многим: User → Post

- FastAPI
- SQLAlchemy
- SQLite

pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload