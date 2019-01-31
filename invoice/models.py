from django.db import models
from client.models import Client


class Invoice(models.Model):
    Invoice_Id = models.CharField(max_length=10, primary_key=True)
    Invoice_Number = models.CharField(max_length=10)
    Invoice_Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Invoice_Exist = models.BooleanField(default=True)   
