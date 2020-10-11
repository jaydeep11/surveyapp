from django.urls import path, re_path
from . import views

urlpatterns = [
    
    path('', views.UserWelcome.as_view(), name='UserWelcome'),
    
    #Auth API
    path('auth/',views.UserLoginView.as_view(),name='User Auth'),

]
