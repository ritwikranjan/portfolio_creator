from django.shortcuts import render
from datetime import date
from .models import PersonalDetail

# Create your views here.
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    print(age)
    return age


def home_view(request):
    personal_details = PersonalDetail.objects.first()
    return render(request, 'myportfolio/index.html', {
        'name': personal_details.name,
        'age': calculate_age(personal_details.dob),
        'email': personal_details.email,
        'linkedin': personal_details.linkedin,
        'github': personal_details.github
    })


