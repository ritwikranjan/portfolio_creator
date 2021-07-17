from datetime import date

from django.shortcuts import render

from .models import Skill, WorkExperience, Project, Reference, Education
from .redirect_views import *
from .forms import SkillForm


# Create your views here.
def calculate_age(birth_date):
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


def home_view(request, slug):
    personal_details = PersonalDetail.objects.get(slug=slug)
    skills = Skill.objects.filter(user=personal_details).all()
    work_experiences = WorkExperience.objects.filter(user=personal_details).all()
    educations = Education.objects.filter(user=personal_details).all()
    projects = Project.objects.filter(user=personal_details).all()
    references = Reference.objects.filter(user=personal_details).all()
    skill_form = SkillForm()
    return render(request, 'myportfolio/index.html', {
        'personal_details': personal_details,
        'age': calculate_age(personal_details.dob),
        'skills': skills,
        'workExperiences': work_experiences,
        'references': references,
        'projects': projects,
        'educations': educations,
        'skill_form': skill_form
    })


def contact(request, slug):
    name = request.POST.get('name')
    email = request.POST.get('email')
    msg = request.POST.get('msg')
    # send_mail(f'Reached from Portfolio: {name}', msg, email, ['ritwikr@ieee.org'])
    return redirect('home', slug)


def add_data(request, slug, field):
    if field == 'skill':
        user = PersonalDetail.objects.get(slug=slug)
        form = SkillForm(request.POST)
        skill = form.save(commit=False)
        skill.user = user
        skill.proficiency = "<Auto Enter>"
        skill.save()

    return redirect('home', slug)
