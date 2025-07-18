from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    
    phone_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^9\d{9}$',
                message='Phone number must start with 9 and be exactly 10 digits.'
            )
        ]
    )

    def __str__(self):
        return self.username
