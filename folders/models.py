from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
