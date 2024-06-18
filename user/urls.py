from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('voting', views.voting, name = 'voting'),
    path('getUserVotingChoice', views.getUserVotingChoices, name = 'getUserVotingChoice'),
    path('empty', views.empty, name = "empty"),
    path('poll/<int:poll_id>/', views.poll_detail_reg, name='poll_detail_reg'),
    path('poll/delete/<int:poll_id>/', views.delete_poll, name='delete_poll'),
    path('all', views.allvotesreg, name = "allvotesreg"),
    path('all/<int:poll_id>/', views.poll_detail_all, name='poll_detail_all'),
    path('vote/<int:poll_id>/', views.vote_all, name='vote_all'),
]