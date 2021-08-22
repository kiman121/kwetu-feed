from app import db
from datetime import datetime

class Category(db.Model):
    '''
    Class that creates a pitch Category Object
    '''
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    category_name = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Post', backref='category', lazy='dynamic')


    def get_categories():
        '''
        Method that retrieves post categories (all)
        '''
        categories = Category.query.all()
        return categories