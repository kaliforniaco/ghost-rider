from django.urls import path
from . import views

urlpatterns = [
  path('api/cars/', views.CarList.as_view(), name='car-list'),
  path('api/cars/<int:pk>', views.CarDetail.as_view(), name='car-detail'),
]