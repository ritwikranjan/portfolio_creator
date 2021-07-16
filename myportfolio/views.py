from datetime import date

from django.shortcuts import render

from .models import Skill, WorkExperience, Project, Reference, Education
from .redirect_views import *


# Create your views here.
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    print(age)
    return age


def home_view(request, slug):
    personal_details = PersonalDetail.objects.get(slug=slug)
    skills = Skill.objects.filter(user=personal_details).all()
    work_experiences = WorkExperience.objects.filter(user=personal_details).all()
    educations = Education.objects.filter(user=personal_details).all()
    projects = Project.objects.filter(user=personal_details).all()
    references = Reference.objects.filter(user=personal_details).all()
    return render(request, 'myportfolio/index.html', {
        'personal_details': personal_details,
        'age': calculate_age(personal_details.dob),
        'skills': skills,
        'workExperiences': work_experiences,
        'references': references,
        'projects': projects,
        'educations': educations
    })




def contact(request, slug):
    name = request.POST.get('name')
    email = request.POST.get('email')
    msg = request.POST.get('msg')
    # send_mail(f'Reached from Portfolio: {name}', msg, email, ['ritwikr@ieee.org'])
    return redirect('home', slug)

