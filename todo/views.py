from rest_framework import (generics, permissions)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Todo
from .serializers import TodoSerializers


# Create your views here.
class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id})


class ListCreateTodo(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = TodoSerializers
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class RetrieveUdateDestroyTodo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()
    
