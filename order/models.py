from django.db import models
from client.models import Client
from product.models import Product


class Order(models.Model):
    Order_Id = models.CharField(max_length=50, primary_key=True)
    Order_Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Order_Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Order_Amount = models.CharField(max_length=10)
    Order_Date = models.DateTimeField()
    Order_Deadline = models.DateTimeField()
    Order_Reference = models.CharField(max_length=128)

    def __str__(self):
        return self.Order_Id
