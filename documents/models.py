from os import rename
from pathlib import Path
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=300)
    user = models.ForeignKey(User,related_name="docs",on_delete=models.CASCADE)
    file = models.FileField(upload_to='pdf_folder',verbose_name='document-file')


    def __str__(self) -> str:
        return self.title

class TextPages(models.Model):
    document = models.ForeignKey(Document,related_name="pages",on_delete=models.CASCADE)
    content =models.TextField()
    page_number = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.document.title
