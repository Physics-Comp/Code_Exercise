from django.urls import path
from . import views

urlpatterns = [
    path('', views.ad_record, name='ad_record'),
    path('delete/<int:pk>/', views.delete_ad_record, name='delete_ad_record'),
]
