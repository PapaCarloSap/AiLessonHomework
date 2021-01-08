from enum import unique
import re
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, String, Integer, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship


Base = declarative_base()

class MixIdUrl:
    id= Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, nullable=False, unique=True)

tag_post = Table(
    'tag_post',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('post.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

class Post(Base, MixIdUrl):
    __tablename__ = 'post'
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'))
    post_image = Column(String)
    date = Column(Date)
    num_watch = Column(Integer)
    author = relationship('Author')
    tags = relationship('Tag', secondary=tag_post)
    comments =relationship('Comment')

class Author(Base, MixIdUrl):
    __tablename__ = 'author'
    name = Column(String, nullable = False)
    posts = relationship('Post')
    comments = relationship('Comment')

class Tag(Base, MixIdUrl):
    __tablename__ = 'tag'
    name = Column(String, nullable=False)
    posts = relationship('Post', secondary=tag_post)

class Comment(Base):
    __tablename__ = 'comment'
    id= Column(Integer, primary_key=True, autoincrement=True)
    data_comment_id = Column(Integer, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    author = relationship('Author')
    post = relationship('Post')