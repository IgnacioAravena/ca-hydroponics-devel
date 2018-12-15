from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    response = models.CharField(max_length=300)
    last_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.owner.username, self.last_date)
