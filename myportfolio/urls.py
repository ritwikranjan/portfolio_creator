from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact', views.contact, name='contact'),
    path('github', views.github_page),
    path('fb', views.fb_page),
    path('insta', views.insta_page),
    path('twitter', views.twitter_page),
    path('linkedin', views.linkedin_page),
]
