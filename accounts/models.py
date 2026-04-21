from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
''' Abtrastract user has the following fields:
username
email
password
first_name
last_name
'''

class User(AbstractUser):
    ROLE_CHOICES = (
        ('SUPERUSER','Superuser'),
        ('ORG_HEAD','Org Head'),
        ('EMPLOYEE','Employee'),
    )
    role = models.CharField(max_length=20, choices = ROLE_CHOICES, default='EMPLOYEE')
    organization = models.ForeignKey(
        'organizations.Organization',
        on_delete = models.SET_NULL,
        null= True,
        blank = True,
        related_name = 'users'
    )

    def __str__(self):
        return self.username
