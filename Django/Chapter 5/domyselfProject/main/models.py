from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=200, unique=True)
    user_pw = models.TextField()
    user_name = models.CharField(max_length=30)
    user_validation = models.BooleanField(default=False)

