from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
import Data_mining.hw3.models as models


class Database:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)

    def _get_or_create(self, session, model, data, key:str):
        db_model = session.query(model).filter(model.url == data[key]).first()
        if not db_model:
            db_model = model(**data)
        return db_model

    def _get_or_create_comment(self, session, data, post):
        db_comment = session.query(models.Comment).filter(models.Comment.data_comment_id == data['data_comment_id']).first()
        if not db_comment:
            db_comment = models.Comment(**data)
            db_comment.author = self._get_or_create(session, models.Author, data['author'], 'url')
            db_comment.post = post
        return db_comment

    def create_post(self, data: dict):
        session = self.maker()
        tags = map(lambda tag_data: self._get_or_create(session,
                                                       models.Tag,
                                                       tag_data,
                                                       'url'
                                                       ), data['tags'])
        author = self._get_or_create(session, models.Author, data['author'], 'url')
        post = self._get_or_create(session, models.Post, data['post_data'], 'url')
        post.author = author
        post.tags.extend(tags)
        comments = map(lambda comment: self._get_or_create_comment(session,
                                                       comment,
                                                       post
                                                       ), data['comments'])
        
        post.comments.extend(comments)
        session.add(post)
 
        try:
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()