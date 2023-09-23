from django.urls import path
from .views import RandomProduct, NextProduct

urlpatterns = [
    path('product/', RandomProduct.as_view()),
    path('next/<int:pk>', NextProduct.as_view())
]
