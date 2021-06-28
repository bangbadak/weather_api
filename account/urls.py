from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
import account.views
app_name = 'account'
urlpatterns = [
    # path('register/', views.register, name='register'),
    # path('Login/', auth_views.LoginView.as_view(template_name='account/Login.html'), name='Login'),
    # path('find_password/', views.find_password, name='find_password'),
    path('signin/', auth_views.LoginView.as_view(template_name='account/signin.html'), name='signin'),
    # path('signin/', views.signin, name ='signin'),
    path('register/', views.register, name ='register'),
    path('find_password/', views.find_password, name ='find_password'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('logout/', account.views.logout, name='logout'),
]