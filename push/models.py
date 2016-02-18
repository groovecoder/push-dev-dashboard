from __future__ import unicode_literals
from base64 import urlsafe_b64decode
from datetime import datetime
import uuid

import ecdsa

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


JWS_KEY_STATUS_CHOICES = (
    ('pending', 'pending'),
    ('valid', 'valid'),
    ('invalid', 'invalid')
)


def generate_jws_key_token():
    return uuid.uuid4()


class PushApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    jws_key = models.CharField(blank=True, max_length=255,
        help_text="VAPID p256ecdsa value; url-safe base-64 encoded.")
    jws_key_status = models.CharField(max_length=255,
                                      default='pending',
                                      choices=JWS_KEY_STATUS_CHOICES)
    jws_key_token = models.CharField(max_length=255,
                                     editable=False,
                                     default=generate_jws_key_token)
    validated = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return "%s: %s" % (self.user.username, self.name)

    def validate_jws_key(self, encrypted_token):
        try:
            verifying_key = ecdsa.VerifyingKey.from_string(
                urlsafe_b64decode(self.jws_key),
                curve=ecdsa.NIST256p
            )
            if (verifying_key.verify(encrypted_token,
                                     str(self.jws_key_token))):
                self.jws_key_status = 'valid'
                self.validated = timezone.make_aware(
                    datetime.now(),
                    timezone.get_current_timezone()
                )
                self.save()
        except ecdsa.BadSignatureError:
            self.jws_key_status = 'invalid'
            self.save()
