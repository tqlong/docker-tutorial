from django.shortcuts import render
from .ml_models import model, get_prediction


def index(request):
    context = {
        'status': 'Input test results'
    }
    return render(request, 'diabetes/index.html', context)


def predict(request):
    context = {
        'status': 'Input test results'
    }
    if request.method == "POST":
        prediction = get_prediction(model, request.POST)
        context = {
            'status': f"Prediction = {prediction['class_idx']} = {prediction['class_name']}"
        }
        features = ["Pregnancies", "Glucose", "BloodPressure",
                    "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
        for key in features:
            if key in request.POST:
                context[key] = request.POST[key]
    return render(request, 'diabetes/index.html', context)
