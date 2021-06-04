from django.db import models
from django.conf import settings
from django.utils import timezone


class Event(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 254)
    phone = models.IntegerField(default=0)
    event = models.TextField()
    eventdate = models.DateField()
    registered_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.event