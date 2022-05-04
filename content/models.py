from django.db import models
from django import forms
from django.urls import reverse_lazy, reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d')
    file = models.FileField(blank=True)

    def __str__(self):
        return self.title
