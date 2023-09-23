from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=155)
    descriptions = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
