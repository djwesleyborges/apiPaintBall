from django.db import models
from django.db.models.signals import post_save


class Perfil(models.Model):
    phone = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50, blank=True)
