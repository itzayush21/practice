from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

df = pd.read_csv("data/synthetic_health_data2.csv")
X = df.loc[:, 'Age':'BMI']
y = df.loc[:, 'Obesity':'No_issue']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Initialize the RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the model to the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy score

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


def predict(data):
    x = np.array(data)
    x = x.reshape(1, -1)
    print(x)
    res = clf.predict(x)
    health_issues = ['Obesity', 'Cardiac_Issue', 'Liver_Problem', 'Respiratory_Issue', 'Nutritional_Deficiency',
                     'Mental_Health_Concern', 'Hypertension', 'Low_Physical_Activity',
                     'High_Fat_Intake', 'Diabetes', 'Kidney_Problem', 'Lack_of_Exercise', 'No_issue']

    encoded_issues = res[0]

    present_issues = [issue for i, issue in enumerate(
        health_issues) if encoded_issues[i] == 1]
    input_text = "Input Values:\n"
    feature_names = X.columns  # Get the feature names from the DataFrame 'X'

    input_dict = {}
    for i, feature in enumerate(feature_names):
        input_dict[feature] = x[0][i]

    return res, present_issues, input_dict


# The data creation process is present in github
'''A Prediction recommendation will be sent to the user 
in form of pdf which will be downloadable during full 
development'''

'''symptoms based diagonsis analysis will be also availabe
the data is already loaded'''
