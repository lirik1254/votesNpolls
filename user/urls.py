from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('voting', views.voting, name = 'voting'),
    path('getUserVotingChoice', views.getUserVotingChoices, name = 'getUserVotingChoice')
]