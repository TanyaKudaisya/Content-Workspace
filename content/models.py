from django.db import models
from django.conf import settings
from organizations.models import Organization
# Create your models here.

User = settings.AUTH_USER_MODEL
class Content(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name = 'contents'
    )
    organization= models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name='contents'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
