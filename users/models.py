from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
class Users(models.Model):

    id = models.AutoField(primary_key=True)
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=20)
    Confirm_password=models.CharField(max_length=20)
    Email=models.CharField(max_length=50)
    Role=models.IntegerField(default=0)

    
    def check_password(self, raw_password):
        return check_password(raw_password, self.Password)

