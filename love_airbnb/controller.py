from flask import request, redirect, url_for, render_template

from love_airbnb import app
from love_airbnb.models import Ad
from love_airbnb.utils import generate_ad

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ad', methods=['GET'])
def not_found():
    return redirect(url_for('index'))

@app.route('/ad', methods=['POST'])
def create_ad():
    data = request.form

    dear = str(data['dear']) or 'San Francisco'
    message = str(data['message']) or 'Thanks for being a real pal!'
    sender = str(data['sender']) or 'Airbnb'

    ad = Ad(dear, message, sender)
    ad = ad.create()

    return redirect(url_for('view_ad', ad_id=ad.id))

@app.route('/ad/<ad_id>')
def view_ad(ad_id):
    ad = Ad.query.get(ad_id)

    ad_img = generate_ad(ad)

    return render_template('ad.html', ad_img=ad_img)

@app.route('/tableview')
def table_view():
    ads = Ad.query.all()

    return render_template('table.html', ads=ads)
