import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("dataset.csv")
dropped_columns = ['Running Nose', 'Asthma', 'Chronic Lung Disease', 'Heart Disease',
                'Diabetes', 'Hyper Tension', 'Family working in Public Exposed Places',
                'Wearing Masks', 'Sanitization from Market']

data.drop(columns=dropped_columns,inplace=True)
data.replace({'Yes':1,'No':0},inplace=True)

input = data.drop("COVID-19",axis=1)
output = data["COVID-19"]

train_x, test_x, train_y, test_y = train_test_split(input, output, test_size=0.2, stratify=output)

model = RandomForestClassifier(n_estimators=45)
model.fit(train_x,train_y)

# Accuracy of the model 
print ("\nMODEL ACCURACY ", model.score(test_x,test_y))

# Storing this trained model so it can be 
# loaded to make predictions without retraining 
model_name = 'covid_model.joblib'
pickle.dump(model, open(model_name, "wb"))
