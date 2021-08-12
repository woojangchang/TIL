from django.db import models
from django.db.models.deletion import CASCADE
from main.models import User

# Create your models here.
class Document(models.Model):
    file_path = models.FileField(upload_to='upload/%Y%m%d')
    file_name = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
