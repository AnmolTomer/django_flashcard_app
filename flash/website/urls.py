from django.urls import path
from . import views  # From this directory import views file

urlpatterns = [
    path('', views.home, name="home"),
    path('add.html', views.add, name="add"),
    path('subtract.html', views.subtract, name="subtract"),
    path('multiply.html', views.multiply, name="multiply"),
    path('divide.html', views.divide, name="divide"),
]
