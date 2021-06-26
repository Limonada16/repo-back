from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class HashTag(models.Model):
    label = models.CharField(max_length=30)

    def __str__(self):
        return self.label
    
class Post(models.Model):
    content = models.CharField(max_length=50)
    hashTags = models.ManyToManyField(HashTag)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content

