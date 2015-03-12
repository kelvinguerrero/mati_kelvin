# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


def create_auth_token(signal, sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        print token.key

post_save.connect(create_auth_token, sender=User)