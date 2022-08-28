from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class contactEnquiry(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=50)
    subject = models.TextField(max_length=100)
    message = models.TextField()


class HackerNews(models.Model):
    titles = models.CharField(max_length=100)
    remark = HTMLField()
