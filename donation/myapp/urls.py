from django.urls import path

from .views import home,causes,volunteer,news,about,contact,donate

urlpatterns = [
    path('', home, name='home'),
    path('about/',about,name='about'),
    path('causes/',causes,name='causes'),
    path('news/',news,name='news'),
    path('contact/',contact,name='contact'),
    path('donate/',donate,name='donate'),
    path('volunteer/',volunteer,name='volunteer')
]