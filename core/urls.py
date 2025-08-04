from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients_list, name='clients_list'),
      path('admin/batteries/', views.battery_list, name='battery_list'),  # новый маршрут
]
from django.urls import path
from . import views


