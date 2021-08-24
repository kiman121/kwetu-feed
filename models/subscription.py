from app import db
from datetime import datetime

class Subscription(db.Model):
    '''
    Class that creates a subscription Object
    '''
    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    first_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_subscribers():
        '''
        Method that retrieves all subscribers
        '''
        subscribers = Subscription.query.all()
        return subscribers