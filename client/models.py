from django.db import models


class Client(models.Model):
    Client_id = models.CharField(max_length=10, primary_key=True)
    Client_name = models.CharField(max_length=50)
    Client_gstin = models.CharField(max_length=20)
    Client_address = models.TextField(max_length=500)
    Client_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.Client_name
