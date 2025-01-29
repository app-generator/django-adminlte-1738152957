# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    badge = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Asset(models.Model):

    #__Asset_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    serial = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Asset_FIELDS__END

    class Meta:
        verbose_name        = _("Asset")
        verbose_name_plural = _("Asset")


class Task(models.Model):

    #__Task_FIELDS__
    due_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_active = models.BooleanField()

    #__Task_FIELDS__END

    class Meta:
        verbose_name        = _("Task")
        verbose_name_plural = _("Task")



#__MODELS__END
