from rest_framework.permissions import BasePermission

class ContentPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        role_policies = {
            'SUPERUSER': lambda user, org: True,
            'ORG_HEAD' : lambda user, org: org.organization_id == user.organization_id,
            'EMPLOYEE' : lambda user, org: org.created_by_id == user.id,
        }
        '''
        if user.role == "SUPERUSER":
            return True
        elif user.role == "ORG_HEAD":
            return obj.organization_id == user.organization_id
        elif user.role == "EMPLOYEE":
            return obj.created_by_id == user.id
        '''
        policy =role_policies.get(user.role)
        return policy(user,obj) if policy else False