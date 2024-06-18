from django.urls import path
from . import views

urlpatterns = [
    path('', views.authorisation, name='authorisation'),
    path('reg', views.registration, name = 'registration'),
    path('succes', views.succes, name = 'success')
]