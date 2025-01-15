from django.db import models

# Create your models here.

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128, unique=True)