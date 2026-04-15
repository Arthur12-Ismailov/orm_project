from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base


# Many-to-Many таблица
post_tag = Table(
    "post_tag",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id")),
    Column("tag_id", ForeignKey("tags.id"))
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    posts = relationship("Post", back_populates="owner")
    profile = relationship("Profile", back_populates="user", uselist=False)


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    bio = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    user = relationship("User", back_populates="profile")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")
    tags = relationship("Tag", secondary=post_tag, back_populates="posts")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    posts = relationship("Post", secondary=post_tag, back_populates="tags")