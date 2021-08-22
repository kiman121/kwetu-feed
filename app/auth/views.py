from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from . import auth
from models.user import User
from models.category import Category
from .forms import LoginForm, RegistrationForm
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Function that handles a login request
    '''
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()

        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.home'))

        flash('Invalid username or password')

    data = {
        "title": 'ZetuFeed - login',
        "login_form":login_form,
        "categories": Category.get_categories()
    }

    return render_template('auth/login.html', context=data)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Function that handles a register request
    '''
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, other_names=form.other_names.data, email=form.email.data,
                    username=form.username.data, password=form.password.data, profile_pic_path="photos/users/default_user_pic.png")
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    
    data = {
        "title": "ZetuFeed - new account",
        "registration_form":form,
        "categories": Category.get_categories()
    }
    return render_template('auth/register.html', context=data)


@auth.route('/logout')
@login_required
def logout():
    '''
    Function that logs out the user from the application
    '''
    logout_user()
    return redirect(url_for("main.home"))
