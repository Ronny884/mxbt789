from app import app, db
from app.models import DynamicFormData
from flask import render_template, request, jsonify


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save_form_data', methods=['POST'])
def save_form_data():
    form_data = request.form.to_dict()
    dynamic_data = DynamicFormData(data=form_data)
    db.session.add(dynamic_data)
    db.session.commit()
    return jsonify({'status': 'success'})


@app.route('/display_form_data')
def display_form_data():
    all_data = DynamicFormData.query.all()
    return render_template('display_data.html', data=all_data)
