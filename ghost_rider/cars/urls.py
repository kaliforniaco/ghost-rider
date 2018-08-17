from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
  path('api/cars/', views.CarList.as_view(), name='car-list'),
  path('api/cars/<int:pk>', views.CarDetail.as_view(), name='car-detail'),
  url(r'^users/$', views.UserList.as_view()),
  url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()), 
  url(r'^api-auth/', include('rest_framework.urls')), 
]

