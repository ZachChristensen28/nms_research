# SURVEY MODELS
from django.db import models
from django.urls import reverse
# from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class Survey(models.Model):
    user = models.ForeignKey(User, related_name='survey')
    started_at = models.DateTimeField(auto_now=True)
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('survey:task', kwargs={'username': self.user.username, 'pk': self.pk})
