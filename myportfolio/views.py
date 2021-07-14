from django.shortcuts import render, redirect
from datetime import date
from .models import Skill, PersonalDetail, WorkExperience, Project, Reference, Education
from django.core.mail import send_mail
from .redirect_views import *


# Create your views here.
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    print(age)
    return age


def home_view(request):
    personal_details = PersonalDetail.objects.first()
    skills = Skill.objects.all()
    work_experiences = WorkExperience.objects.all()
    educations = Education.objects.all()
    projects = Project.objects.all()
    references = Reference.objects.all()
    return render(request, 'myportfolio/index.html', {
        'personal_details': personal_details,
        'age': calculate_age(personal_details.dob),
        'skills': skills,
        'workExperiences': work_experiences,
        'references': references,
        'projects': projects,
        'educations': educations
    })


def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    msg = request.POST.get('msg')
    # send_mail(f'Reached from Portfolio: {name}', msg, email, ['ritwikr@ieee.org'])
    return redirect('home')

