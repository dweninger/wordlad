
#map requets from views.py to specific URLS
from django.urls import path, include
from wordladApp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    #home
    path('', views.wordlad, name='home'),
    path('/<int:wordlad_number>/', views.wordlad_number, name='wordlad'),
    path('word_exists/<str:word>/', views.word_exists, name='word_exists'),

]

