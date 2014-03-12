from django.contrib.auth.models import User
from django.db import models


class Forum(models.Model):
    moderators = models.ManyToManyField(User, related_name='forums_moderated')
    members = models.ManyToManyField(User, related_name='forums_member')
