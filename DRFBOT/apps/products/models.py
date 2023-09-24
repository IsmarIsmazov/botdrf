from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=155)
    image = models.ImageField()
    descriptions = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(verbose_name="Номер телефона клиента")

