# RiffMates/promoters/models.py
from django.db import models

class Promoter(models.Model):
    common_name = models.CharField(max_length=25)
    full_name = models.CharField(max_length=50)
    famous_for = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=30)
