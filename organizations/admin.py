from django.contrib import admin
from .models import Organization, Membership, Role, Permission, RolePermission
# Register your models here.

admin.site.register(Organization)
admin.site.register(Membership)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(RolePermission)
