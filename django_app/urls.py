from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('status', views.system_status, name='system_status'),
]