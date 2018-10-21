from django.db import models
from datetime import date
# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(("date"),auto_now=False)
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
