import random

from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer

from apps.products import models


# Create your views here.
class RandomProduct(APIView):
    def get(self, *args, **kwargs):
        all_product = models.Product.objects.all()
        random_product = random.choice(all_product)
        serialized_random_product = ProductSerializer(random_product, many=False)

        return Response(serialized_random_product.data)


class NextProduct(APIView):
    def get(self, request, pk, format=None):
        product = models.Product.objects.filter(pk__gt=pk).first()
        if not product:
            return Response(status.HTTP_404_NOT_FOUND())
        ser_product = ProductSerializer(product, many=False)
        return Response(ser_product.data)
