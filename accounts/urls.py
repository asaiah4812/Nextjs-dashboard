from django.urls import path
from . import api

urlpatterns = [
    path('<str:pk>/', api.user_detail)
]
