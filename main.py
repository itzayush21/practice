from flask import Flask, jsonify, render_template, request
from algo import predict
app = Flask(__name__)

# Initialize SQLAlchemy with the Flask app
health_issues_recommendations = {
    'Obesity': {
        'Precaution': [
            'Regularly monitor weight.',
            'Avoid high-calorie foods.',
            'Practice portion control.'
        ],
        'Diet Plan': [
            'Focus on vegetables, lean proteins, whole grains.',
            'Avoid sugary drinks and high-fat foods.',
            'Maintain a caloric deficit.'
        ],
        'Medications (India)': [
            'Orlistat (Alli)',
            'Metformin (Glucophage)',
            'Lorcaserin (Belviq)'
        ],
        'Future Concerns': [
            'Risk of cardiovascular diseases.',
            'Increased risk of diabetes.',
            'Joint problems.'
        ],
        'Exercise Plan': [
            '150 minutes of moderate aerobic activity weekly (e.g., brisk walking, cycling).',
            'Strength training twice a week.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    },
    'Cardiac_Issue': {
        'Precaution': [
            'Regular heart health check-ups.',
            'Avoid excessive salt.',
            'Manage stress and quit smoking.'
        ],
        'Diet Plan': [
            'Fruits, vegetables, whole grains, lean proteins.',
            'Limit saturated fats, cholesterol.'
        ],
        'Medications (India)': [
            'Aspirin',
            'Statins (Atorvastatin)',
            'Beta-blockers (Metoprolol)'
        ],
        'Future Concerns': [
            'Risk of heart attack.',
            'Potential for stroke.',
            'Risk of heart failure.'
        ],
        'Exercise Plan': [
            'Low-impact exercises (e.g., walking, swimming).',
            '150 minutes of moderate-intensity exercise per week.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    },
    'Liver_Problem': {
        'Precaution': [
            'Avoid alcohol.',
            'Maintain a healthy weight.',
            'Regular liver function tests.'
        ],
        'Diet Plan': [
            'Balanced diet with fruits, vegetables, whole grains.',
            'Avoid fatty foods and limit sugar intake.'
        ],
        'Medications (India)': [
            'Ursodeoxycholic Acid (Ursofalk)',
            'Silymarin (Milk Thistle)',
            'Enalapril (Vasotec)'
        ],
        'Future Concerns': [
            'Risk of liver cirrhosis.',
            'Potential for liver failure.',
            'Risk of liver cancer.'
        ],
        'Exercise Plan': [
            'Moderate physical activity (e.g., walking, yoga).',
            'Focus on maintaining a healthy weight.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    },
    'Respiratory_Issue': {
        'Precaution': [
            'Avoid exposure to pollutants.',
            'Quit smoking.',
            'Get vaccinated against respiratory infections.'
        ],
        'Diet Plan': [
            'Foods rich in antioxidants (e.g., berries, nuts).',
            'Maintain proper hydration.'
        ],
        'Medications (India)': [
            'Salbutamol (Ventolin)',
            'Ipratropium (Atrovent)',
            'Montelukast (Singulair)'
        ],
        'Future Concerns': [
            'Risk of chronic obstructive pulmonary disease (COPD).',
            'Asthma exacerbations.',
            'Potential for respiratory infections.'
        ],
        'Exercise Plan': [
            'Low-impact exercises (e.g., walking, swimming).',
            'Breathing exercises and pulmonary rehabilitation.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    },
    'Nutritional_Deficiency': {
        'Precaution': [
            'Regularly monitor nutritional intake.',
            'Consider supplementation if necessary.'
        ],
        'Diet Plan': [
            'Balanced diet rich in vitamins and minerals.',
            'Include diverse food groups.'
        ],
        'Medications (India)': [
            'Vitamin Supplements (e.g., Vitamin D3, B12)',
            'Iron Supplements (e.g., Ferrous Sulfate)'
        ],
        'Future Concerns': [
            'Risk of anemia.',
            'Potential for weakened immune system.'
        ],
        'Exercise Plan': [
            'Moderate exercise to improve overall health.',
            'Focus on balanced nutrition rather than exercise alone.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    },
    'Mental_Health_Concern': {
        'Precaution': [
            'Regular mental health check-ups.',
            'Manage stress effectively.',
            'Seek professional help if needed.'
        ],
        'Diet Plan': [
            'Foods rich in omega-3 fatty acids (e.g., fish, flaxseeds).',
            'Include fruits, vegetables, and whole grains.'
        ],
        'Medications (India)': [
            'Antidepressants (e.g., Fluoxetine, Sertraline)',
            'Anxiolytics (e.g., Diazepam)'
        ],
        'Future Concerns': [
            'Risk of chronic mental health disorders.',
            'Potential for decreased quality of life.'
        ],
        'Exercise Plan': [
            'Regular physical activity to improve mood (e.g., walking, yoga).',
            'Consider relaxation techniques and mindfulness.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    },
    'Hypertension': {
        'Precaution': [
            'Monitor blood pressure regularly.',
            'Reduce sodium intake.',
            'Manage stress.'
        ],
        'Diet Plan': [
            'Low-sodium diet.',
            'Include fruits, vegetables, and whole grains.'
        ],
        'Medications (India)': [
            'Antihypertensives (e.g., Amlodipine, Losartan)',
            'Diuretics (e.g., Hydrochlorothiazide)'
        ],
        'Future Concerns': [
            'Risk of heart disease.',
            'Potential for stroke.',
            'Kidney damage.'
        ],
        'Exercise Plan': [
            'Regular aerobic activity (e.g., walking, swimming).',
            'Strength training exercises.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    },
    'Low_Physical_Activity': {
        'Precaution': [
            'Incorporate more movement into daily routine.',
            'Set realistic activity goals.'
        ],
        'Diet Plan': [
            'Balanced diet with moderate calorie intake.',
            'Include proteins, healthy fats, and fibers.'
        ],
        'Medications (India)': [
            'Generally not applicable unless related to a specific condition.'
        ],
        'Future Concerns': [
            'Risk of obesity.',
            'Potential for cardiovascular issues.'
        ],
        'Exercise Plan': [
            'Gradually increase physical activity.',
            'Include both aerobic and strength training exercises.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    },
    'High_Fat_Intake': {
        'Precaution': [
            'Monitor fat intake.',
            'Choose healthy fats (e.g., avocados, nuts).'
        ],
        'Diet Plan': [
            'Limit saturated and trans fats.',
            'Include healthy fats and fibers.'
        ],
        'Medications (India)': [
            'Statins (e.g., Atorvastatin)',
            'Omega-3 supplements'
        ],
        'Future Concerns': [
            'Risk of cardiovascular disease.',
            'Potential for weight gain.'
        ],
        'Exercise Plan': [
            'Regular physical activity.',
            'Focus on overall cardiovascular health.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    },
    'Diabetes': {
        'Precaution': [
            'Regular monitoring of blood glucose levels.',
            'Follow a diabetic-friendly diet.'
        ],
        'Diet Plan': [
            'Low glycemic index foods.',
            'Include whole grains, lean proteins, and vegetables.'
        ],
        'Medications (India)': [
            'Metformin (Glucophage)',
            'Insulin',
            'Sulfonylureas (e.g., Glibenclamide)'
        ],
        'Future Concerns': [
            'Risk of heart disease.',
            'Potential for neuropathy.'
        ],
        'Exercise Plan': [
            'Regular aerobic and strength training exercises.',
            'Focus on blood sugar control.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    },
    'Kidney_Problem': {
        'Precaution': [
            'Monitor kidney function regularly.',
            'Avoid excessive salt and protein intake.'
        ],
        'Diet Plan': [
            'Low-sodium, low-protein diet.',
            'Include fruits and vegetables.'
        ],
        'Medications (India)': [
            'Diuretics (e.g., Furosemide)',
            'ACE inhibitors (e.g., Ramipril)'
        ],
        'Future Concerns': [
            'Risk of kidney failure.',
            'Potential for fluid imbalances.'
        ],
        'Exercise Plan': [
            'Moderate physical activity.',
            'Avoid excessive strain.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    },
    'Lack_of_Exercise': {
        'Precaution': [
            'Gradually increase physical activity.',
            'Set achievable exercise goals.'
        ],
        'Diet Plan': [
            'Balanced diet to support increased activity levels.',
            'Include a mix of proteins, carbs, and healthy fats.'
        ],
        'Medications (India)': [
            'Generally not applicable unless related to a specific condition.'
        ],
        'Future Concerns': [
            'Risk of obesity and cardiovascular issues.',
            'Potential for mental health concerns.'
        ],
        'Exercise Plan': [
            'Start with light exercises and gradually increase intensity.',
            'Include aerobic and strength training exercises.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    },
    'No_issue': {
        'Precaution': [
            'Maintain a healthy lifestyle.',
            'Regular health check-ups.'
        ],
        'Diet Plan': [
            'Balanced diet to support overall health.',
            'Include a variety of nutrients.'
        ],
        'Medications (India)': [
            'Generally not applicable.'
        ],
        'Future Concerns': [
            'Continue maintaining a healthy lifestyle.'
        ],
        'Exercise Plan': [
            'Regular physical activity.',
            'Maintain a balanced exercise routine.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    }
}


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template("/index.html")


@app.route('/survey')
def survey():
    return render_template('survey.html')


def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100  # convert height to meters
    bmi = weight_kg / (height_m ** 2)
    return bmi


@app.route('/info', methods=['GET', 'POST'])
def info():
    gender_mapping = {'Male': 0, 'Female': 1}
    sleep_quality_mapping = {'Good': 1, 'Poor': 2, 'Average': 0}
    stress_level_mapping = {'Low': 1, 'High': 0, 'Medium': 2}
    activity_level_mapping = {'Sedentary': 1, 'Active': 0}
    exercise_type_mapping = {'None': 1, 'Strength Training': 2, 'Cardio': 0}
    smoking_habits_mapping = {'Regular smoker': 2,
                              'Non-smoker': 0, 'Occasional smoker': 12}

    if request.method == 'POST':
        # Accessing form data
        age = request.form.get('age')
        gender = request.form.get('gender')
        height_cm = request.form.get('height_cm')
        weight_kg = request.form.get('weight_kg')
        sleep_hours = request.form.get('sleep_hours')
        sleep_quality = request.form.get('sleep_quality')
        stress_level = request.form.get('stress_level')
        activity_level = request.form.get('work_type')
        alcohol_consumption = request.form.get('alcohol_consumption')
        smoking_habits = request.form.get('smoking_habits')
        daily_caloric_intake = request.form.get('daily_caloric_intake')
        protein_intake_g = request.form.get('protein_intake_g')
        carb_intake_g = request.form.get('carb_intake_g')
        fat_intake_g = request.form.get('fat_intake_g')
        fruit_veg_intake = request.form.get('fruit_veg_intake')
        daily_steps = request.form.get('daily_steps')
        exercise_type = request.form.get('exercise_type')
        exercise_duration_min = request.form.get('exercise_duration_min')
        heart_rate_bpm = request.form.get('heart_rate_bpm')
        blood_pressure_systolic = request.form.get('blood_pressure_systolic')
        blood_pressure_diastolic = request.form.get('blood_pressure_diastolic')
        blood_sugar_mg_dl = request.form.get('blood_sugar_mg_dl')
        cholesterol_mg_dl = request.form.get('cholesterol_mg_dl')
        liver_function_ast = request.form.get('liver_function_ast')
        liver_function_alt = request.form.get('liver_function_alt')
        mental_health_score = request.form.get('mental_health_score')
        bmi = 27.1

        numeric_gender = gender_mapping[gender]
        numeric_sleep_quality = sleep_quality_mapping[sleep_quality]
        numeric_stress_level = stress_level_mapping[stress_level]
        numeric_activity_level = activity_level_mapping[activity_level]
        numeric_exercise_type = exercise_type_mapping[exercise_type]
        numeric_smoking_habits = smoking_habits_mapping[smoking_habits]

        values_array = [age,
                        numeric_gender,
                        height_cm,
                        weight_kg,
                        sleep_hours,
                        numeric_sleep_quality,
                        numeric_stress_level,
                        numeric_activity_level,
                        alcohol_consumption,
                        numeric_smoking_habits,
                        daily_caloric_intake,
                        protein_intake_g,
                        carb_intake_g,
                        fat_intake_g,
                        fruit_veg_intake,
                        daily_steps,
                        numeric_exercise_type,
                        exercise_duration_min,
                        heart_rate_bpm,
                        blood_pressure_systolic,
                        blood_pressure_diastolic,
                        blood_sugar_mg_dl,
                        cholesterol_mg_dl,
                        liver_function_ast,
                        liver_function_alt,
                        mental_health_score,
                        bmi
                        ]

    # We are going to send precaution, medicine etc here during full development
        s, issue, input = predict(values_array)
        return render_template('survey.html', input=input, issue=issue, result=health_issues_recommendations)
    return render_template('survey.html')
    # return render_template('survey.html')


@app.route('/symptom')
def symptom():
    return render_template('symptom.html')


if __name__ == '__main__':
    app.run(debug=True)
