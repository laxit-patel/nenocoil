from django.db import models
from client.models import Client

class Drawing(models.Model):
    Drawing_Id = models.CharField(primary_key=True, max_length=50)
    Drawing_File = models.FileField()
    Drawing_Revision = models.CharField(max_length=10)
    Drawing_Origin = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.Drawing_Id