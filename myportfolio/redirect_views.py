from django.shortcuts import redirect
from .models import PersonalDetail


def fb_page(request, slug):
    personal_details = PersonalDetail.objects.get(slug=slug)
    return redirect(f'https://{personal_details.fb}')


def insta_page(request, slug):
    personal_details = PersonalDetail.objects.get(slug=slug)
    return redirect(f'https://{personal_details.insta}')


def github_page(request, slug):
    personal_details = PersonalDetail.objects.get(slug=slug)
    return redirect(f'https://{personal_details.github}')


def linkedin_page(request, slug):
    personal_details = PersonalDetail.objects.get(slug=slug)
    return redirect(f'https://{personal_details.linkedin}')


def twitter_page(request, slug):
    personal_details = PersonalDetail.objects.get(slug=slug)
    return redirect(f'https://{personal_details.twitter}')
