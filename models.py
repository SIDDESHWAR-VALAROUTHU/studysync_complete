from django.db import models

class Table(models.Model):
    username=models.CharField(max_length=25)
    email=models.EmailField(max_length=40)
    phone=models.IntegerField(default=10)
    password=models.CharField(max_length=40)
    
        