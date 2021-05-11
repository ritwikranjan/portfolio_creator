from django.shortcuts import render
from datetime import date


# Create your views here.
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def home_view(request):
    return render(request, 'myportfolio/index.html', {
        'name': 'Ritwik Ranjan',
        'age': calculate_age(date(2000, 6, 26)),
        'email': 'ritwikranjan99@gmail.com',

    })


