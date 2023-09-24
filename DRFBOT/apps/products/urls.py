from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RandomProduct, NextProduct, products, create_product, order

# router = DefaultRouter()
# router.register('products', ProductViewSet)
urlpatterns = [
    path('random/', RandomProduct.as_view()),
    path('next/<int:pk>', NextProduct.as_view()),
    path('create-product/', create_product, name='create-product'),
    path('products/', products, name='products'),
    path('order/', order, name="order"),

]
# urlpatterns += router.urls
