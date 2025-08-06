from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients_list, name='clients_list'),
    path('admin/batteries/', views.battery_list, name='battery_list'),  # новый маршрут
    # path('clients2/', views.clients2_list, name='clients2_list'),  # Commented out as it's not defined in views.py
]
