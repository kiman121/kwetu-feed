from flask import render_template, request, url_for, abort
from . import main
from .forms import LoginForm, RegistrationForm
from models.category import Category
from models.comment import Comment
from models.post import Post
from models.user import User


@main.route('/')
def home():
    '''
    View function that renders the index page
    '''
    title = "ZetuFeed - home"
    categories = Category.get_categories()

    return render_template('index.html', title=title, categories=categories)
