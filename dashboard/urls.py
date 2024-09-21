from django.urls import path
from . import api

urlpatterns = [
    path('', api.user_list),
    # path('<str:pk>/', api.user_detail),
    path('products/', api.product_list)
]
