from django.db import models

# Create your models here.
class Grettings(models.Model):
    heading = models.CharField(max_length=30)
