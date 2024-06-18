from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name = 'profile_noreg'),
    path('votes', views.votes, name = 'votes_noreg'),
    path('votes/<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('vote/<int:poll_id>/', views.vote, name='vote'),
]