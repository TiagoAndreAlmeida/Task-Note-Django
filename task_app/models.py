from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nome", max_length=100, blank=False, null=False)
    photo = models.ImageField(blank=True, null=True, upload_to='profile')

    def __str__(self):
        return self.name