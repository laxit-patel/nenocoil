from django.db import models


class User(models.Model):
    User_Id = models.CharField(max_length=10)
    User_Name = models.CharField(max_length=32)
    User_Email = models.EmailField(max_length=50)
    User_Role = models.CharField(max_length=32)
    User_Password = models.CharField(max_length=64)
    User_Exist = models.BooleanField(default=True)

    def __str__(self):
        return self.User_Name
