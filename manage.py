from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from models.category import Category
from models.comment import Comment
from models.post import Post
from models.user import User


# Creating app instance
app = create_app(('development'))
manager = Manager(app)
migrate = Migrate(app, db)

def datetimeformat(value, format):
    if format == 'long':
        format='%B %d, %Y'
    elif format == 'short':
        format='%b %Y'
    return value.strftime(format)
app.jinja_env.filters['datetimeformat'] = datetimeformat

if __name__ == '__main__':
    manager.run()