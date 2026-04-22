from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Content
from .permissions import ContentPermission
from .serializers import ContentSerializer
# Create your views here.

class ContentViewSet(ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated, ContentPermission]

    def get_queryset(self):
        user = self.request.user
        membership = user.memberships.first()
        if not membership:
            return Content.objects.filter(created_by=user)
        if membership.role.name == 'ORG_HEAD':
            return Content.objects.filter(
            organization=membership.organization
            )
        if membership.role.name == 'EMPLOYEE':
            return Content.objects.filter(
            created_by=user
            )

        return Content.objects.none()
        
        # query_map = {
        #     'SUPERUSER': Content.objects.all(),
        #     'ORG_HEAD': Content.objects.filter(
        #         organization = user.organization
        #     ),
        #     'EMPLOYEE': Content.objects.filter(
        #         created_by=user
        #     )
        # }
        # return query_map.get(user.role, Content.objects.none())
    
    
    #assign the role of creator
    def perform_create(self, serializer):
        user = self.request.user
        membership = user.memberships.first()
        serializer.save(
            created_by=user,
            organization=membership.organization if membership else None
        )
