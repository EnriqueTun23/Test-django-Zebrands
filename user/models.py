import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

#  The base of the django model was used combining the email
class User(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'users'