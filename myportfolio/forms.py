from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Skill, Education, Project, WorkExperience, Reference, PersonalDetail


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level']


class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ['user']


class ReferenceForm(ModelForm):
    class Meta:
        model = Reference
        exclude = ['user']


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['user']


class ExperienceForm(ModelForm):
    class Meta:
        model = WorkExperience
        exclude = ['user']


class ProfileForm(ModelForm):
    class Meta:
        model = PersonalDetail
        exclude = ['user', 'slug', 'id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'row': 3}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control'}),
            'insta': forms.URLInput(attrs={'class': 'form-control'}),
            'fb': forms.URLInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'maps': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
