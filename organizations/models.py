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
    


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    
class Permission(models.Model):
    ACTION_CHOICES = (
        ('CREATE','Create'),
        ('READ','Read'),
        ('UPDATE','Update'),
        ('DELETE','Delete'),
    )
    action = models.CharField(max_length=20, choices = ACTION_CHOICES)
    resource = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.action} {self.resource}"

class RolePermission(models.Model):
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='role_permissions'
    )
    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.role} {self.permission}"
    
class Membership(models.Model):
    ROLE_CHOICES=(
        ('ORG_HEAD','Org Head'),
        ('EMPLOYEE','Employee')
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='memberships'
    )
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        related_name='memberships'
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.user} - {self.organization} - {self.role}"