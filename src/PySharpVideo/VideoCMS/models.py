from simplemongo.models import Document
from django.contrib import admin
from django.db import models
import datetime

class File(Document):
    __validate__ = True
    struct = {
        'id'          : int,
        'size'        : int,
        'token'       : str,
        'filehash'    : str,
        'created_at'  : datetime.datetime,
        'finished_at' : datetime.datetime
    }

# Create your models here.

class File(models.Model):
    id              = models.IntegerField(primary_key=True)
    size            = models.BigIntegerField()

admin.site.register(File)
