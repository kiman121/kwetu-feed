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

    def __init__(self, category_name):
        '''
        Method that defines Category object properties.
        Args: 
            category_name: New category name
        '''
        self.category_name = category_name

    def get_categories():
        '''
        Method that retrieves post categories (all)
        '''
        categories = Category.query.all()
        return categories
   
    def get_category_by_id(catid):
        '''
        Method that retrieves category by id
        '''
        if catid == 0:
            category = {"id":0,"category_name":"All categories"}
        else:
            category = Category.query.filter_by(id=catid).first()
        
        return category

    def save_category(self):
        '''
        Method that saves the instance of category model
        '''
        db.session.add(self)
        db.session.commit()