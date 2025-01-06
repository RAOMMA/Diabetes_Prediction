import argparse
import joblib

# Load the pre-trained logistic regression model
model = joblib.load('C:\salman\ML\Diabetes Prediction\model.pkl')

# Create an argument parser
parser = argparse.ArgumentParser(description="Diabetes Prediction")

# Add the --value argument to accept a data record
parser.add_argument('-Pregnancies', type = int,default=6)
parser.add_argument('-Glucose', type = int,default=148)
parser.add_argument('-BloodPressure', type = int,default=72)
parser.add_argument('-SkinThickness', type = int,default=35)
parser.add_argument('-Insulin', type = int,default=0)
parser.add_argument('-BMI', type = float,default=33.6)
parser.add_argument('-DiabetesPedigreeFunction', type = float,default=0.627)
parser.add_argument('-Age', type = int,default=50)

# Parse the command-line arguments
args = parser.parse_args()

def input_data(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    list=[]
    list.append(Pregnancies)
    list.append(Glucose)
    list.append(BloodPressure)
    list.append(SkinThickness)
    list.append(Insulin)
    list.append(BMI)
    list.append(DiabetesPedigreeFunction)
    list.append(Age)
    return list
df=[input_data(args.Pregnancies,args.Glucose,args.BloodPressure,args.SkinThickness,args.Insulin,args.BMI,args.DiabetesPedigreeFunction,args.Age)]



# Make a prediction using the loaded model
prediction = model.predict(df)

# Print the result
if prediction[0] == 1:
    print("diabeties")
elif prediction[0] == 0:
    print("No diabetes")
else:
    print("Unknown class")