from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from models.category import Category
from models.user import User
from models.category import Category


# Creating app instance
app = create_app(('production'))

# @app.before_first_request
# def create_tables():
#     db.create_all()

manager = Manager(app)
migrate = Migrate(app, db)

def datetimeformat(value, format):
    if format == 'long':
        format='%B %d, %Y'
    elif format == 'short':
        format='%b %Y'
    return value.strftime(format)
app.jinja_env.filters['datetimeformat'] = datetimeformat

@manager.command
def test():
    '''
    Run the unit tests.
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    '''
    Function that allows us to pass properties into the shell context.
    '''
    return dict(app=app, db=db, User=User, Category=Category)

if __name__ == '__main__':
    manager.run()