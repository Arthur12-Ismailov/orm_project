from sqlalchemy.orm import Session
import models, schemas


# CREATE
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(title=post.title, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


# READ
def get_users(db: Session):
    return db.query(models.User).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# UPDATE
def update_user(db: Session, user_id: int, name: str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.name = name
        db.commit()
        db.refresh(user)
    return user


# DELETE
def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


# QUERIES
def get_posts_by_user(db: Session, user_id: int):
    return db.query(models.Post).filter(models.Post.user_id == user_id).all()


def get_posts_by_tag(db: Session, tag_name: str):
    return db.query(models.Post).join(models.Post.tags).filter(models.Tag.name == tag_name).all()