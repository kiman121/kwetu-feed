from app import db
from datetime import datetime

class Comment(db.Model):
    '''
    Class that creates comment objects
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
