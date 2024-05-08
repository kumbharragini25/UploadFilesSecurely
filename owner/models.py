from django.contrib.auth.hashers import check_password
from django.db import models

class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=128)  
    Confirm_password = models.CharField(max_length=128)  
    Email = models.CharField(max_length=50)
    Role = models.IntegerField(default=0)

    def check_password(self, raw_password):
        return check_password(raw_password, self.Password)