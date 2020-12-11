from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:user_id>', views.profile, name='profile'),
    path('<int:user_id>/following', views.following, name='following'),
    path('<int:user_id>/follower', views.follower, name='follower'),
    path('<int:user_id>/follow-button', views.follow_button, name='follow-button'),
    path('<int:user_id>/archive', views.archive, name='archive'),

]