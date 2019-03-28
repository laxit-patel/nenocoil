from django.db import models
from drawing.models import Drawing


class Design(models.Model):
    Design_Id = models.CharField(max_length=50, primary_key=True)
    Design_Dimension = models.CharField(max_length=100)
    Design_Connection = models.CharField(max_length=100)
    Design_Fpi = models.CharField(max_length=50)
    Design_Tube = models.CharField(max_length=100)
    Design_Hairpin = models.CharField(max_length=100)
    Design_Drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE)

    def __str__(self):
        return self.Design_Id
