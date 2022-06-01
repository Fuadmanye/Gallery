from django.urls import path
from . import views

urlpatterns = [
  
    path('',views.index, name = 'home'),
    path('landing',views.landing, name = 'landing'),
    path('nature', views.nature_images, name = "nature"),
    path('park', views.park_images, name = "park"),
    path('beach', views.beach_images, name = "beach"),
    path('cgi', views.cgi_images, name = "cgi"),
    path('search/',views.search_results, name = 'search_results'),
]