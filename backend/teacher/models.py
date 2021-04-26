from django.db import models


class Teacher(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='teacher', blank=True, null=True, default=None)
