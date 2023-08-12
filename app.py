from flask import Flask,request,render_template
from utils import get_heart_disease
import config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/disease_prediction",methods =["GET","POST"])
def disease():
    if request.method == "GET":
        data = request.args.get

        age = data("age")
        sex = data("sex")
        cp = data("cp")
        trestbps = data("trestbps")
        chol = data("chol")
        fbs = data("fbs")
        restecg = data("restecg")
        thalach = data("thalach")
        exang = data("exang")
        oldpeak = data("oldpeak")
        slope = data("slope")
        ca = data("ca")
        thal = data("thal")
    
        

        prediction = get_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal)

        if prediction == 0:
            Disease_Status = "N0_Disease"
        if prediction == 1:
            Disease_Status = "Disease"
        
        


        return render_template("index.html",Disease_Prediction = Disease_Status)
    

    elif request.method == "POST":
        data = request.form

        age = data("age")
        sex = data["sex"]
        cp = data["cp"]
        trestbps = data["trestbps"]
        chol = data["chol"]
        fbs = data["fbs"]
        restecg = data["restecg"]
        thalach = data["thalach"]
        exang = data["exang"]
        oldpeak = data["oldpeak"]
        slope = data["slope"]
        ca = data["ca"]
        thal = data["thal"]
        

        prediction = get_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal)

        if prediction == 0:
            Disease_Status = "N0_Risk"
        if prediction == 1:
            Disease_Status = "Risk"
        
        


        return render_template("index.html",Disease_Prediction = Disease_Status)


if __name__ == "__main__":
    app.run(host = config.HOST_NUMBER,port = config.PORT_NUMBER,debug=True)