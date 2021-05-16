from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length=10000, default="")

    users_to_fly = models.PositiveSmallIntegerField()

    class Status(models.TextChoices):
        GROUNDED = 'G', 'Grounded'
        TAKING_OFF = 'T', 'Taking off'
        FLYING = 'F', 'Flying'

    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.GROUNDED,
    )

    def __str__(self):
        return self.title

    @property
    def time_since_published(self):
        return timezone.now() - self.pub_date

    @property
    def boarded_users(self):
        return Boarding.objects.filter(post=self)

    @property
    def num_boarded_users(self):
        return len(self.boarded_users)

    @property
    def is_ready_to_fly(self):
        return self.users_to_fly <= self.num_boarded_users

    def is_user_boarded(self, user):
        return Boarding.objects.filter(
            post=self,
            user=user
        ).exists()

class Boarding(models.Model):

    def __str__(self):
        return "Boarding " + str(self.user) + " " +str(self.post)

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )