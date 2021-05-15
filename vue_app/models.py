from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length=10000, default="")

    def __str__(self):
        return self.title

    def time_since_published(self):
        return timezone.now() - self.pub_date
