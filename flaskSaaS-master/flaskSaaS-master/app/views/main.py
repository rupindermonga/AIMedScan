from flask import render_template, jsonify
from app import app
import random
import keras


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/uploaded', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		model = ResNet50(weights = 'weights.h5')
		img = image.load_img(f.filename)
		preds = model.predict(img)
		return render_template('uploaded.html', predictions= preds_decoded)


@app.route('/map')
def map():
    return render_template('map.html', title='Map')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')