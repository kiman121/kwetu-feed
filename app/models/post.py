from . import db
from datetime import datetime

class Post(db.Model):
    '''
    Class that creates a post object
    '''
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    comments = db.relationship('Comment', backref='comment', lazy='dynamic')
