from django.urls import path

from .views import home,news,about,contact,donate,elimu,health,family

urlpatterns = [
    path('', home, name='home'),
    path('about/',about,name='about'),
    path('news/',news,name='news'),
    path('elimu/',elimu,name='elimu'),
    path('health/',health,name='health'),
    path('contact/',contact,name='contact'),
    path('family/',family,name='family'),
    path('donate/',donate,name='donate'),
]