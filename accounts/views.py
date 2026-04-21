from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"User Created"}, status=201)
        return Response(serializer.errors, status=400)
    



class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"user": str(request.user)})
