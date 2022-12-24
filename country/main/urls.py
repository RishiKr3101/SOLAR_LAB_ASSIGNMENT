from django.urls import path

from . import views

urlpatterns = [
    path('country_info/<countryname>', views.home, name='home'),
    
    
]