from django.db import models


class ProductType(models.Model):
    ProductType_Id = models.CharField(primary_key=True, max_length=50)
    Product_Type = models.CharField(max_length=100)

    def __str__(self):
        return self.ProductType_Id

