from app import db
from datetime import datetime
from sqlalchemy import desc

class Post(db.Model):
    '''
    Class that creates a post object
    '''
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String(), nullable=False)
    post = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def featured_post():
        '''
        Method that retrieves last post to be displayed as the first post
        '''
        featured_post = Post.query.order_by(Post.id.desc()).first()
    
        return featured_post

    def get_posts():
        '''
        Method that retrieves all posts
        '''
        posts = Post.query.order_by(Post.id.desc()).all()
    
        return posts
    