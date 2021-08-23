from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user
from . import main
from ..import db, photos
from ..request import get_quote, post_comment_count
from .forms import PostForm, AddCommentForm, DeletePostForm, EditPostForm, DeleteCommentForm
from models.category import Category
from models.comment import Comment
from models.post import Post
from models.user import User
from datetime import datetime
from sqlalchemy import func


@main.route('/')
def home():
    '''
    View function that renders the index page
    '''
    data = {
        "title": "ZetuFeed - home",
        "categories": Category.get_categories(),
        "new_post_form": PostForm(),
        "random_quote": get_quote(),
        "featured_post": Post.featured_post(),
        "posts": Post.get_posts(),
        "delete_form": DeletePostForm(),
        "edit_post_form": EditPostForm(),
        "add_comment": AddCommentForm(),
        "post_comments": Comment.get_comments(),
        "post_comment_count": post_comment_count(),
        "delete_comment_post": DeleteCommentForm()
    }

    return render_template('index.html', context=data)


@main.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    '''
    View function that handles an add new post request
    '''
    form = PostForm()
    request_endpoint = form.endpoint.data

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


@main.route('/post/delete', methods=['Get', 'POST'])
@login_required
def delete_post():
    '''
    View function that handles delete post request
    '''
    form = DeletePostForm()
    post = Post.query.filter_by(id=form.post_id.data).first()
    Comment.query.filter(Comment.post_id == form.post_id.data).delete()
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('.home'))


@main.route('/post/edit', methods=['Get', 'POST'])
@login_required
def edit_post():
    '''
    View function that handles edit post request
    '''
    form = EditPostForm()
    post = Post.query.filter_by(id=form.post_id.data).first()

    request_endpoint = form.endpoint.data

    if request_endpoint == 'main.profile':
        redirect_to = url_for('.profile', userid=current_user.id)
    elif request_endpoint == 'main.home':
        redirect_to = url_for('.home')

    if form.validate_on_submit():
        post.title = form.title.data
        post.post = form.post.data
        post.updated_at = datetime.utcnow()
        post.category_id = form.category.data.id

        db.session.add(post)
        db.session.commit()

    return redirect(redirect_to)


@main.route('/post/comment', methods=['GET', 'POST'])
@login_required
def add_comment():
    '''
    View function that handles add comment request
    '''
    form = AddCommentForm()

    request_endpoint = form.endpoint.data

    if request_endpoint == 'main.profile':
        redirect_to = url_for('.profile', userid=current_user.id)
    elif request_endpoint == 'main.home':
        redirect_to = url_for('.home')

    if form.validate_on_submit():

        new_comment = Comment(post_id=form.post_id.data, user_id=current_user.get_id(
        ), comments=form.comment.data)

        db.session.add(new_comment)
        db.session.commit()

    return redirect(redirect_to)


@main.route('/post/comment/delete', methods=['GET', 'POST'])
@login_required
def delete_comment():
    '''
    View function that handles delete comment
    '''
    form = DeleteCommentForm()
    comment = Comment.query.filter_by(id=form.comment_id.data).first()
    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for('.home'))

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    '''
    View function that renders a user profile
    '''
    data = {
        "title": "ZetuFeed - home",
        "categories": Category.get_categories()
    }
    
    return render_template('profile.html', context = data)