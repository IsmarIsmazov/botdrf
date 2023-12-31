import asyncio
import random

from decouple import config
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .postbackend import send_notification
from .models import Product
from .serializers import ProductSerializer, OrderSerializer


# Create your views here.
class RandomProduct(APIView):
    def get(self, *args, **kwargs):
        all_product = Product.objects.all()
        random_product = random.choice(all_product)
        serialized_random_product = ProductSerializer(random_product, many=False)

        return Response(serialized_random_product.data)


@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NextProduct(APIView):
    def get(self, request, pk, format=None):
        product = Product.objects.filter(pk__gt=pk).first()
        if not product:
            return Response(status.HTTP_404_NOT_FOUND())
        ser_product = ProductSerializer(product, many=False)
        return Response(ser_product.data)


@api_view(["POST"])
def order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        chat_id = config('CHAT_KEY')
        message_text = f'у вас новый клиент!\n' \
                       f'{request.data["username"]}\n' \
                       f'он заказал: ' \
                       f'{request.data["product"]}\n' \
                       f'вы сможете с ним связаться через: \n' \
                       f'{request.data["email"]}\n' \
                       f'{request.data["phone_number"]}\n'

        async def send_notification_async():
            await send_notification(chat_id, message_text)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_notification_async())
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
