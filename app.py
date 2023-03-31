from flask import Flask, request, render_template
import requests
import joblib
import pandas as pd
from sklearn.preprocessing import Normalizer
import numpy as np

app = Flask(__name__,template_folder='/HETIC/Mastère 2/Machine Learning/deploy/template')
model = joblib.load('model.joblib')
transformer = Normalizer()

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the form data
        overall_material = request.form.get('overall_material')
        construction_date = request.form.get('construction_date')
        remodel_date = request.form.get('remodel_date')
        masonry_veneer = request.form.get('masonry_veneer')
        total_sq_ft = request.form.get('total_sq_ft')
        first_floor_sq = request.form.get('first_floor_sq')
        above_grade = request.form.get('above_grade')
        full_bathrooms = request.form.get('full_bathrooms')
        total_rooms = request.form.get('total_rooms')
        year_garage = request.form.get('year_garage')
        garage_capacity = request.form.get('garage_capacity')
        garage_sq_ft = request.form.get('garage_sq_ft')
        house_age = request.form.get('house_age')

        # Convert form data to a Pandas DataFrame
        data = pd.DataFrame({
            'Overall Material': [overall_material],
            'Construction Date': [construction_date],
            'Remodel Date': [remodel_date],
            'Masonry Veneer': [masonry_veneer],
            'Total Sq Ft': [total_sq_ft],
            'First Floor Sq': [first_floor_sq],
            'Above Grade': [above_grade],
            'Full Bathrooms': [full_bathrooms],
            'Total Rooms': [total_rooms],
            'Year Garage': [year_garage],
            'Garage Capacity': [garage_capacity],
            'Garage Sq Ft': [garage_sq_ft],
            'House Age': [house_age]
        })
        # Make a prediction using the model
        #datas = 
        prediction = model.predict(transformer.transform(data))
        # Render the results template with the prediction
        return render_template('results.html', prediction=prediction[0])

    # Render the form template for GET requests
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)