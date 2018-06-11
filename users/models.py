import uuid
from django.db import models
from django.contrib.sites.models import Site

class User(models.Model):
    username = models.CharField(max_length=500)
    token = models.CharField(max_length=500, default=uuid.uuid4())
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.username
