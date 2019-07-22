import uuid

from django.db import models
from cloudinary.models import CloudinaryField


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    banner = CloudinaryField('imagem')
    #banner = models.ImageField(upload_to='bannerJogos/', blank=True)

    def __str__(self):
        return self.name
