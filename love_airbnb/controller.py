from flask import request, redirect, url_for, render_template

from love_airbnb import app
from love_airbnb.models import Ad
from love_airbnb.utils import generate_ad


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ad', methods=['GET'])
def opps_shouldnt_get():
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    ad = Ad('User',
            '404: This page was not found. ' +
            'Guess you should be more careful...',
            'The Webmaster')

    ad_img = generate_ad(ad)

    return render_template('ad.html', ad_img=ad_img), 404


@app.errorhandler(500)
def server_error(e):
    ad = Ad('User',
            '500: Opps, so I messed up, ' +
            'but you\'ll probably try again anyways',
            'The Webmaster')

    ad_img = generate_ad(ad)

    return render_template('ad.html', ad_img=ad_img), 500


@app.route('/ad', methods=['POST'])
def create_ad():
    data = request.form

    dear = unicode(data['dear']) or 'San Francisco'
    message = unicode(data['message']) or 'Thanks for being a real pal!'
    sender = unicode(data['sender']) or 'Airbnb'

    ad = Ad(dear, message, sender)
    ad = ad.create()

    return redirect(url_for('view_ad', ad_id=ad.id))


@app.route('/ad/<ad_id>')
def view_ad(ad_id):
    ad = Ad.query.get(ad_id)

    ad_img = generate_ad(ad)

    return render_template('ad.html', ad_img=ad_img)
