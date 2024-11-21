from django.urls import path
from . import views

urlpatterns = [
    path('', views.introduce_yourself, name='introduce_yourself'),
]
