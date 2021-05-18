from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name="home-page"),
   path('whatnews/', views.what_news, name="whatnews-page"),
]
