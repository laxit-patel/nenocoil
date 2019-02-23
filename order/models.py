from django.db import models


class Order(models.Model):
    Order_Id = models.CharField(max_length=50, primary_key=True)
    Order_Client_Name = models.CharField(max_length=50)
    Order_Amount = models.CharField(max_length=10)

    def __str__(self):
        return self.Order_Id
