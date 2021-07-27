from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

STATUS_CHOICES = ('created', 'running', 'completed')

class Task(models.Model):

    class Status(models.IntegerChoices):
        CREATED = 0, _('created')
        RUNNING = 1, _('running')
        FINISHED = 2, _('finished')

    name = models.CharField(
        max_length=150
        )
    created = models.DateTimeField(
        auto_now_add=True
        )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
        )
    status = models.IntegerField(
        choices=Status.choices,
        default=0
        )