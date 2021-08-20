from flask import render_template, request, url_for, abort
from . import main


@main.route('/')
def home():
    '''
    View function that renders the index page
    '''
    return render_template('index.html')