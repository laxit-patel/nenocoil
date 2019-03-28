from django.db import models
from django.forms import ModelForm
from django import forms


class Client(models.Model):
    Client_Id = models.CharField(max_length=50, primary_key=True)
    Client_Name = models.CharField(max_length=50)
    Client_Gstin = models.CharField(max_length=50)
    Client_Address = models.TextField(max_length=500)
    Client_Email = models.EmailField(max_length=254)
    Client_Phone = models.CharField(max_length=50)
    Client_Exist = models.BooleanField(default=True)

    def __str__(self):
        return self.Client_Id



