from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('voting', views.voting, name = 'voting'),
    path('getUserVotingChoice', views.getUserVotingChoices, name = 'getUserVotingChoice'),
    path('empty', views.empty, name = "empty"),
    path('poll/<int:poll_id>/', views.poll_detail_reg, name='poll_detail_reg')
]