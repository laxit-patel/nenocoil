from django.db import models
from producttype.models import ProductType
from design.models import Design


class Product(models.Model):
    Product_Id = models.CharField(max_length=50, primary_key=True)
    Product_Design = models.ForeignKey(Design, on_delete=models.CASCADE)
    Product_Price = models.CharField(max_length=50)
    Product_Type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.Product_Id


