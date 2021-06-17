from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('Login/', auth_views.LoginView.as_view(template_name='account/Login.html'), name='Login'),
    path('find_password/', views.find_password, name='find_password')
]