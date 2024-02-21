from django.urls import path

from .views import home,news,about,contact,donate,elimu,health,family,signin,register,signout

urlpatterns = [
    path('', home, name='home'),
    path('signin/',signin,name='signin'),
    path('register/',register,name='register'),
    path('signout/',signout,name='signout'),
    path('about/',about,name='about'),
    path('news/',news,name='news'),
    path('elimu/',elimu,name='elimu'),
    path('health/',health,name='health'),
    path('contact/',contact,name='contact'),
    path('family/',family,name='family'),
    path('donate/',donate,name='donate'),
]