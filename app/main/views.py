from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user
from . import main
from ..import db, photos
from ..request import get_quote, post_comment_count, individual_post_comment_count
from .forms import PostForm, AddCommentForm, DeletePostForm, EditPostForm, DeleteCommentForm, EditProfileForm, SubscriptionForm
from models.category import Category
from models.comment import Comment
from models.post import Post
from models.user import User
from models.subscription import Subscription
from datetime import datetime
from sqlalchemy import func
from ..email import mail_message


@main.route('/', defaults={'catid':0})
@main.route('/<int:catid>')
def home(catid):
    '''
    View function that renders the index page
    '''
    if catid == 0:
        active_tab = 0
    else:
        active_tab = catid

    data = {
        "title": "ZetuFeed - home",
        "categories": Category.get_categories(),
        "new_post_form": PostForm(),
        "random_quote": get_quote(),
        "selected_category_name": Category.get_category_by_id(catid),
        "featured_post": Post.featured_post(catid),
        "posts": Post.get_posts(catid),
        "active_tab":active_tab,
        "delete_form": DeletePostForm(),
        "edit_post_form": EditPostForm(),
        "add_comment": AddCommentForm(),
        "post_comments": Comment.get_comments(),
        "post_comment_count": post_comment_count(catid),
        "delete_comment_post": DeleteCommentForm(),
        "add_subscription": SubscriptionForm()
    }

    return render_template('index.html', context=data)

@main.route('/post/<int:pid>')
def post(pid):
    '''
    View function that renders a post
    ''' 
    data = {
        "title": "ZetuFeed - post",
        "categories": Category.get_categories(),
        "new_post_form": PostForm(),
        "random_quote": get_quote(),
        "post": Post.get_post_by_id(pid),

        "delete_form": DeletePostForm(),
        "edit_post_form": EditPostForm(),
        "add_comment": AddCommentForm(),
        "post_comments": Comment.get_comments(),
        "post_comment_count": individual_post_comment_count(pid),
        "delete_comment_post": DeleteCommentForm(),
        "add_subscription": SubscriptionForm()
    }

    return render_template('post.html', context=data)

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
        active_tab = form.active_tab.data
        if active_tab == 0:
            redirect_to = url_for('.home')
        else:
            redirect_to = url_for('.home', catid=active_tab)

    if form.validate_on_submit():

        new_post = Post(post=form.post.data, user_id=current_user.get_id(
        ), category_id=form.category.data.id, title=form.title.data)

        db.session.add(new_post)
        db.session.commit()
        
        subscribers = Subscription.get_subscribers()
        for subscriber in subscribers:
            mail_message("ZetuFeed - new post",
                     "email/new_post", subscriber.email, subscriber=subscriber, post=new_post)

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

    request_endpoint = form.endpoint.data

    if request_endpoint == 'main.post':
        redirect_to = url_for('.home')
    elif request_endpoint == 'main.home':
        active_tab = form.active_tab.data
        if active_tab == 0:
            redirect_to = url_for('.home')
        else:
            redirect_to = url_for('.home', catid=active_tab)


    return redirect(redirect_to)


@main.route('/post/edit', methods=['Get', 'POST'])
@login_required
def edit_post():
    '''
    View function that handles edit post request
    '''
    form = EditPostForm()
    post = Post.query.filter_by(id=form.post_id.data).first()

    request_endpoint = form.endpoint.data

    if request_endpoint == 'main.post':
        redirect_to = url_for('.post', pid=form.post_id.data)
    elif request_endpoint == 'main.home':
        active_tab = form.active_tab.data
        if active_tab == 0:
            redirect_to = url_for('.home')
        else:
            redirect_to = url_for('.home', catid=active_tab)

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

    if request_endpoint == 'main.post':
        redirect_to = url_for('.post', pid=form.post_id.data)
    elif request_endpoint == 'main.home':
        active_tab = form.active_tab.data
        if active_tab == 0:
            redirect_to = url_for('.home')
        else:
            redirect_to = url_for('.home', catid=active_tab)
    print("outside")
    if form.validate_on_submit():
        print("inside")
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
    request_endpoint = form.endpoint.data

    if request_endpoint == 'main.post':
        redirect_to = url_for('.post', pid=comment.post_id)
    elif request_endpoint == 'main.home':
        active_tab = form.active_tab.data
        if active_tab == 0:
            redirect_to = url_for('.home')
        else:
            redirect_to = url_for('.home', catid=active_tab)
    
    db.session.delete(comment)
    db.session.commit()

    return redirect(redirect_to)

@main.route('/profile/<int:uid>', methods=['GET', 'POST'])
@login_required
def profile(uid):
    '''
    View function that renders a user profile
    '''
    data = {
        "title": "ZetuFeed - profile",
        "categories": Category.get_categories(),
        "user_details": User.get_user_by_id(uid),
        "edit_profile_form": EditProfileForm()
    }
    return render_template('profile.html', context = data)

@main.route('/profile/edit', methods=['Get', 'POST'])
@login_required
def edit_profile():
    '''
    View function that handles edit post request
    '''
    form = EditProfileForm()
    user = User.query.filter_by(id=current_user.get_id()).first()

    if form.validate_on_submit():
        user.first_name = form.first_name.data
        user.other_names = form.other_names.data
        user.bio = form.bio.data
        user.updated_at = datetime.utcnow()

        if 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            path = f'photos/users/{filename}'
            user.profile_pic_path = path

        db.session.add(user)
        db.session.commit()

    return redirect(url_for('.profile', uid=current_user.get_id()))

@main.route('/subscription', methods=['GET','POST'])
def subscribe():
    '''
    View function that handles a subscription
    '''
    form = SubscriptionForm()
    if form.validate_on_submit():
        subscriber = Subscription(first_name=form.first_name.data, email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()

        mail_message("Welcome to ZetuFeed",
                     "email/welcome_subscriber", subscriber.email, subscriber=subscriber)

        return redirect(url_for('.home'))