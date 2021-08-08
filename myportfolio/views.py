from datetime import date

from django.contrib.auth import login
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Skill, WorkExperience, Project, Reference, Education
from .redirect_views import *
from .forms import SkillForm, EducationForm, ExperienceForm, ProjectForm, ReferenceForm, ProfileForm, MyUserCreationForm


# Create your views here.
def calculate_age(birth_date):
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


def home_view(request, slug):
    personal_details = get_object_or_404(PersonalDetail, slug=slug)
    skills = Skill.objects.filter(user=personal_details).all()
    work_experiences = WorkExperience.objects.filter(user=personal_details).all()
    educations = Education.objects.filter(user=personal_details).all()
    projects = Project.objects.filter(user=personal_details).all()
    references = Reference.objects.filter(user=personal_details).all()
    return render(request, 'myportfolio/edit_portfolio.html', {
        'personal_details': personal_details,
        'age': calculate_age(personal_details.dob),
        'skills': skills,
        'workExperiences': work_experiences,
        'references': references,
        'projects': projects,
        'educations': educations,
    })


@login_required
def edit_view(request, slug):
    personal_details = PersonalDetail.objects.get(slug=slug)
    if request.user == personal_details.user:
        skills = Skill.objects.filter(user=personal_details).all()
        work_experiences = WorkExperience.objects.filter(user=personal_details).all()
        educations = Education.objects.filter(user=personal_details).all()
        projects = Project.objects.filter(user=personal_details).all()
        references = Reference.objects.filter(user=personal_details).all()
        skill_form = SkillForm()
        education_form = EducationForm()
        experience_form = ExperienceForm()
        project_form = ProjectForm()
        reference_form = ReferenceForm()
        return render(request, 'myportfolio/index.html', {
            'edit': True,
            'personal_details': personal_details,
            'age': calculate_age(personal_details.dob),
            'skills': skills,
            'workExperiences': work_experiences,
            'references': references,
            'projects': projects,
            'educations': educations,
            'skill_form': skill_form,
            'education_form': education_form,
            'experience_form': experience_form,
            'project_form': project_form,
            'reference_form': reference_form
        })
    else:
        return HttpResponseForbidden(request)


def contact(request, slug):
    name = request.POST.get('name')
    email = request.POST.get('email')
    msg = request.POST.get('msg')
    # send_mail(f'Reached from Portfolio: {name}', msg, email, ['ritwikr@ieee.org'])
    return redirect('home', slug)


@login_required
def add_data(request, slug, field):
    user = PersonalDetail.objects.get(slug=slug)
    if request.user == user.user:
        if field == 'skill':
            form = SkillForm(request.POST)
            if form.is_valid():
                skill = form.save(commit=False)
                skill.user = user
                skill.proficiency = "<Auto Enter>"
                skill.save()
                print(skill)
        elif field == 'education':
            form = EducationForm(request.POST)
            if form.is_valid():
                education = form.save(commit=False)
                education.user = user
                education.save()
        elif field == 'experience':
            form = ExperienceForm(request.POST)
            if form.is_valid():
                experience = form.save(commit=False)
                experience.user = user
                experience.save()
            else:
                print(form.errors)
        elif field == 'project':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = user
                project.save()
        elif field == 'reference':
            form = ReferenceForm(request.POST, request.FILES)
            if form.is_valid():
                reference = form.save(commit=False)
                reference.user = user
                reference.save()
            else:
                print(form.errors)

    return redirect('edit', slug)


def create_portfolio(request):
    if request.method == 'POST':
        user_creation_form = MyUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_creation_form.is_valid() and profile_form.is_valid():
            username = user_creation_form.cleaned_data.get('username')
            password = user_creation_form.cleaned_data.get('password')
            email = profile_form.cleaned_data.get('email')
            user = User.objects.create_user(username, email, password)
            login(request, user)
            profile = profile_form.save(commit=False)
            profile.id = user.pk
            profile.user = user
            profile.save()
            return redirect('home', username)
        else:
            print(profile_form.errors, user_creation_form.errors)
    else:
        user_creation_form = MyUserCreationForm()
        profile_form = ProfileForm()

    return render(request, 'myportfolio/registration/user_creation.html', {
        'user_creation_form': user_creation_form,
        'profile_form': profile_form
    })


def start_page(request):
    if request.user.is_authenticated:
        return redirect('home', request.user.profile.slug)
    else:
        return render(request, 'myportfolio/home.html', {})


@login_required
def delete_data(request, slug, field, pk):
    if request.user == get_object_or_404(PersonalDetail, slug=slug).user:
        if field == 'skill':
            obj = Skill.objects.get(pk=pk)
            obj.delete()
        elif field == 'education':
            obj = Education.objects.get(pk=pk)
            obj.delete()
        elif field == 'experience':
            obj = WorkExperience.objects.get(pk=pk)
            obj.delete()
        elif field == 'project':
            obj = Project.objects.get(pk=pk)
            obj.delete()
        elif field == 'reference':
            obj = Reference.objects.get(pk=pk)
            obj.delete()

    return redirect('edit', slug)
