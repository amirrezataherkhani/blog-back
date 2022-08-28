from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, AllowAny
from main.serializers import PostSerializer, CommentSerializer, UserSerializer, RegisterSerializer
from main.models import Post, Comment
from django.contrib.auth.models import User


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class UserList(generics.ListAPIView):
    permission_classes = [IsAdminUser, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
