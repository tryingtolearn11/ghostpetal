from flask import render_template
from app import app
import os

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'GHOST PETAL'}
    posts = [ 
        {
             'author': {'username': 'JOHNNY'},
             'body': 'THIS IS A TEST POST!'
        },
        {
            'author': {'username': 'MAX'},
            'body': 'THIS SUCKS!!!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)




@app.route('/stream')
def stream():
    return "CLICKED STREAM"





@app.route('/download')
def download():
    return "DOWNLOAD LINK :D"



@app.route('/gallery')
def gallery():
    images = os.listdir('/home/damien/ghostpetal/app/static/ghostpetalsimages')
    print(images)
    return render_template('gallery.html', images=images)

