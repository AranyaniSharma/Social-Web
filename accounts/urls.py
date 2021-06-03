from django.urls import path
from django.contrib.auth import views as auth_views #login view and logout view is located here we do not need to create in views .py
from . import views#import my views from views .py files


app_name='accounts'

urlpatterns=[
       path('login/',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
        path('logout/',
        auth_views.LogoutView.as_view(),name='logout'),#it will go to the home pge when we logout
        path('signup/', views.SignUp.as_view(), name="signup"),


]
