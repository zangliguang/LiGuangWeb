from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class user(models.Model):
    # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User)
    address = models.CharField(max_length=200, default='', blank=True)
    sex = models.SmallIntegerField(default=0)
    birthday = models.DateField(default=datetime.now)
    email = models.EmailField(blank=True)
    image = models.ImageField(blank=True)
    phonenum = PhoneNumberField(blank=True)

    def __str__(self):
        return self.user.username