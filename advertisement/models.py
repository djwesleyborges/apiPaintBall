from django.db import models
from django.urls import reverse
from user.models import User


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    complement = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=9)
    price = models.CharField(max_length=8)
    description = models.TextField()
    image = models.ImageField(upload_to='media/%Y/%m/%d/', default='', verbose_name='Imagem')
    created_at = models.DateTimeField('Created on: ', auto_now_add=True)
    update_at = models.DateTimeField('Update on: ', auto_now=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # slug = models.SlugField('Unique identifier', max_length=100)

    class Meta:
        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisements'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:advert', kwargs={'slug': self.slug})
