import uuid

from django.db import models
from user.models import User



class Publication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    create_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    # answer = models.OneToOneField(Answer, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
        ordering = ['created']

    def __str__(self):
        return self.title



class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='answer')
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    create_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ['created']

    def __str__(self):
        return self.description


class RelationshipPubAns(models.Model):
    publication = models.ManyToManyField(Publication, related_name='publication')
    answer = models.ManyToManyField(Answer, related_name='answer')