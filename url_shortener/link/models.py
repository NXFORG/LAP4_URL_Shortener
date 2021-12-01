from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.CharField(max_length=200)
    website = models.CharField(max_length=20)