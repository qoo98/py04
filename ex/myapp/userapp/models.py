from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Shop(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name







    # def get_absolute_url(self):
    #     return reverse('userapp:detail', kwargs={'pk', self.pk})
        # self.pkを１としたらPKを１としてdetailviewを呼び出している。


