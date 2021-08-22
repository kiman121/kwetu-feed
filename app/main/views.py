from flask import render_template, request, url_for, abort
from flask_login import login_required, current_user
from . import main
from ..import db, photos
from ..request import get_quote
from .forms import PostForm, AddComment
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
    new_post_form = PostForm()
    categories = Category.get_categories()
    random_quote = get_quote()

    return render_template('index.html', title=title, categories=categories, new_post_form=new_post_form, random_quote=random_quote)

@main.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    '''
    View function that handles an add new post request
    '''
    form = PostForm()
    request_endpoint = form.endpoint.data
    print(request_endpoint)
    if request_endpoint == 'main.profile':
        redirect_to = url_for('.profile', userid=current_user.id)
    elif request_endpoint == 'main.home':
        redirect_to = url_for('.home')

    if form.validate_on_submit():

        print(request_endpoint)

        new_post = Post(post=form.post.data, user_id=current_user.get_id(
        ), category_id=form.category.data.id, title=form.title.data)

        db.session.add(new_post)
        db.session.commit()

    return redirect(redirect_to)