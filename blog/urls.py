from django.urls import path
from . import views

urlpatterns = [
   path('', views.blog_home, name='blog-home'), # this name='blog-home' was assign name.
   path('<int:blog_detail_id>/', views.detail, name='detail-page'),
   path('detail_page/', views.list_detail, name="search-results"), # this line for search bar.
]
