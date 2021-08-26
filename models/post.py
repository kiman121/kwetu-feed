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

    def featured_post(catid):
        '''
        Method that retrieves last post to be displayed as the first post
        '''
        if catid == 0:
            featured_post = Post.query.order_by(Post.id.desc()).first()
        else:
            featured_post = Post.query.filter_by(category_id=catid).order_by(Post.id.desc()).first()

        return featured_post

    def get_posts(catid):
        '''
        Method that retrieves all posts
        '''
        if catid == 0:
            posts = Post.query.order_by(Post.id.desc()).all()
        else:
            posts = Post.query.filter_by(category_id=catid).order_by(Post.id.desc()).all()

        return posts
    
    def get_post_by_id(pid):
        '''
        Method that retrieves a post by id
        '''
        post = Post.query.filter_by(id=pid).first()
        
        return post