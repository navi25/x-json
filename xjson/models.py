from django.db import models

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ConvertedFile(models.Model):
    filename = models.CharField(max_length=255, blank=True)
    fileurl = models.CharField(max_length=255, blank=True)
    converted_at = models.DateTimeField(auto_now_add=True)
