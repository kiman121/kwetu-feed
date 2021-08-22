from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, validators
from wtforms.validators import Required
from wtforms_sqlalchemy.fields import QuerySelectField
from models.user import User
from models.category import Category 
from wtforms import ValidationError

class PostForm(FlaskForm):
    '''
    Class to create a post form
    '''
    def category_query():
        return Category.query

    category = QuerySelectField(query_factory = category_query,blank_text="Select category", get_label='category_name',validators=[validators.DataRequired()])
    post = TextAreaField('Your post',  validators=[Required()])
    title = StringField('Title', validators=[Required()])
    endpoint = StringField('Endpoint', validators=[Required()])
    submit = SubmitField('Post')

class AddComment(FlaskForm):
    '''
    Class to create add comment form
    '''
    comment = StringField('Add comment', validators=[Required()])
    submit = SubmitField('Add')

# class UpdateProfile(FlaskForm):
#     '''
#     Class to create an update profile form
#     '''
#     first_name = StringField("First name", validators=[Required()])
#     other_names = StringField("Other names", validators=[Required()])
#     submit = SubmitField('Submit')
