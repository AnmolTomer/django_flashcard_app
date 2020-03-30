from django.urls import path
from . import views  # From this directory import views file

urlpatterns = [
    path('', views.home, name="home"),
]
