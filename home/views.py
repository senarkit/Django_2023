from django.shortcuts import render, HttpResponse
import joblib
from static.main import func

# Create your views here.
def home(requests):
    return render(requests, 'home.html')

def SGN(requests):
    return render(requests, 'SGN.html')

def HASE(requests):
    return render(requests, 'HASE.html')

def MSB(requests):
    # return HttpResponse("This is page for M&S Market")
    return render(requests, "MSB.html")

def PRED(requests):
    if requests.method == "POST":
        func(method = "Ridge-Regression")
        model = joblib.load("static/model.joblib")

        age = int(requests.POST.get('age'))
        sex = int(requests.POST.get('sex'))
        bmi = int(requests.POST.get('bmi'))
        children = int(requests.POST.get('children'))
        smoker = int(requests.POST.get('smoker'))
        region = int(requests.POST.get('region'))
        print(age, bmi, sex, children, smoker, region)

        pred = model.predict([[age, bmi, sex, children, smoker, region]])
        print(pred)

        output = {
            "output": round(pred[0],2),
            "val": {"Age":age, 
                    "BMI":bmi,
                    "Sex":sex,
                    "Children":children,
                    "Smoker?":smoker,
                    "Region":region}
            }
        return render(requests, "predictions.html", output)
    else:
        return render(requests, "predictions.html")