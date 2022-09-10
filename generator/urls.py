from django.urls import path
from generator.views import home, generatedPassword, about

urlpatterns = [
    path('', home, name='home'),
    path('generate-password', generatedPassword, name='password'),
    path('about', about, name='about'),
]