from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nome", max_length=100, blank=False, null=False)
    photo = models.ImageField(blank=True, null=True, upload_to='profile')

    def __str__(self):
        return self.name

class Task (models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, blank=False, null=False)
    description = models.CharField(verbose_name="Descrição", max_length=100, blank=False, null=False)
    done = models.BooleanField(verbose_name="Feito", default=False)
    dead_line = models.DateField(verbose_name="Vencimento")
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title