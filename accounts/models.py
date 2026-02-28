from django.db import models
from django.contrib.auth.models import AbstractUser # new

class costomUser(AbstractUser): # new
    name = models.CharField(null=True, blank=True, max_length=100)
