from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    # Get Urls
    path('<slug:slug>/', views.home_view, name='home'),
    path('', views.start_page, name='start'),

    # POST Urls
    path('<slug:slug>/contact', views.contact, name='contact'),
    path('<slug:slug>/add/<str:field>', views.add_data, name='add'),
    path('<slug:slug>/edit', views.edit_view, name='edit'),

    # DELETE Urls
    path('<slug:slug>/delete/<str:field>/<int:pk>', views.delete_data, name='delete'),

    # Auth Urls
    path('accounts/login/', LoginView.as_view(template_name='myportfolio/registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='start'), name='logout'),
    path('accounts/signup/', views.create_portfolio, name='sign_up'),

    # Redirect URLs
    path('<slug:slug>/github', views.github_page, name='github'),
    path('<slug:slug>/fb', views.fb_page, name='fb'),
    path('<slug:slug>/insta', views.insta_page, name='insta'),
    path('<slug:slug>/twitter', views.twitter_page, name='twitter'),
    path('<slug:slug>/linkedin', views.linkedin_page, name='linkedin'),
]
