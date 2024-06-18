
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usernoreg.urls')),
    path('user', include('user.urls')),
    path('authorisation', include('registration.urls'))
]
