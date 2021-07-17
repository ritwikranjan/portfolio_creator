from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>/', views.home_view, name='home'),
    path('<slug:slug>/contact', views.contact, name='contact'),
    path('<slug:slug>/add/<str:field>', views.add_data, name='add'),
    path('<slug:slug>/github', views.github_page),
    path('<slug:slug>/fb', views.fb_page),
    path('<slug:slug>/insta', views.insta_page),
    path('<slug:slug>/twitter', views.twitter_page),
    path('<slug:slug>/linkedin', views.linkedin_page),
]
