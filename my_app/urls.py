# my_app/urls.py
from django.urls import path
from .views import upload_profile, profile_list

urlpatterns = [
    path('upload/', upload_profile, name='upload_profile'),
    path('', profile_list, name='profile_list'),
    path('upload/', upload_profile, name='upload_profile'),


]
