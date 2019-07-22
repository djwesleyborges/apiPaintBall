import uuid

from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.signals import post_save


class Perfil(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50, blank=True)
    # imagem = CloudinaryField('imagem')

