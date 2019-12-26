from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('count/', views.count, name = 'counting'),
    path('about/', views.about, name = 'aboutpage')
]
