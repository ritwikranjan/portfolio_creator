from django.shortcuts import redirect
from .models import PersonalDetail


def fb_page(request):
    personal_details = PersonalDetail.objects.first()
    return redirect(f'https://{personal_details.fb}')


def insta_page(request):
    personal_details = PersonalDetail.objects.first()
    return redirect(f'https://{personal_details.insta}')


def github_page(request):
    personal_details = PersonalDetail.objects.first()
    return redirect(f'https://{personal_details.github}')


def linkedin_page(request):
    personal_details = PersonalDetail.objects.first()
    return redirect(f'https://{personal_details.linkedin}')


def twitter_page(request):
    personal_details = PersonalDetail.objects.first()
    return redirect(f'https://{personal_details.twitter}')
