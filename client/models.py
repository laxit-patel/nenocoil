from django.db import models


class Client(models.Model):
    Client_Id = models.CharField(max_length=50, primary_key=True)
    Client_Name = models.CharField(max_length=50)
    Client_Gstin = models.CharField(max_length=20)
    Client_Address = models.TextField(max_length=500)
    Client_Email = models.EmailField(max_length=254)
    Client_Exist = models.BooleanField(default=True)

