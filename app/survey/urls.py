from django.urls import path, re_path
from . import views

urlpatterns = [
    
    path('', views.UserWelcome.as_view(), name='UserWelcome'),
    
    #Auth API
    path('auth/',views.UserLoginView.as_view(),name='User Auth'),

    path('survey/create/',views.CreateSurveyView.as_view(),name='create survey'),

    path('survey/take/',views.TakeSurveyView.as_view(),name='take survey'),

    path('survey/result/',views.SurveyResultView.as_view(),name='result survey'),

    path('thumbnail/',views.CreateThumbnailView.as_view(),name='create thumbnail'),
]
