from django.db import models
from client.models import Client
from order.models import Order


class Invoice(models.Model):
    Invoice_Id = models.CharField(max_length=10, primary_key=True)
    Invoice_Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Invoice_Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Invoice_Exist = models.BooleanField(default=True)

    def __str__(self):
        return self.Invoice_Id
