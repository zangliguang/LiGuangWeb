# -*- coding: utf-8 -*-
import uuid
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
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

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("User List")

    def __str__(self):
        return self.user.username

class BusinessProject(models.Model):
    bid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, default=_("Default Business Name"), blank=True)


    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("User List")

    def __str__(self):
        return self.user.username