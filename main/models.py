from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    user = models.ForeignKey(User, verbose_name=("user"), on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True,null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)