from django.db import models
from client.models import Client


class Invoice(models.Model):
    Invoice_id = models.CharField(max_length=10, primary_key=True)
    Invoice_number = models.CharField(max_length=10)
    Invoice_Client = models.ForeignKey(Client, on_delete=models.CASCADE)
