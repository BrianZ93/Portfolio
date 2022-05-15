from flask import Blueprint, render_template
from flask_cors import cross_origin

site = Blueprint('site', __name__, template_folder = 'templates')

@site.route('/')
@cross_origin()
def home():
    return render_template('index.html')