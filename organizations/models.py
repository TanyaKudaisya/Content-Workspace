from django.db import models
from django.conf import settings
import uuid
# Create your models here.
User = settings.AUTH_USER_MODEL

def generate_code():
    return uuid.uuid4().hex[:6].upper()

class Organization(models.Model):
    name = models.CharField(max_length=300)
    created_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='organization_created'
    )
    join_code = models.CharField(max_length=10, unique=True, default = generate_code)

    def __str__(self):
        return self.name
