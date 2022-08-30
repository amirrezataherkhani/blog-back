from django.db import IntegrityError
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, AllowAny
from main.serializers import PostSerializer, CommentSerializer, UserSerializer, RegisterSerializer
from main.models import Post, Comment
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status


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

    def create(self, request, *args, **kwargs):
        try:
            data = {}
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                account = serializer.save()
                account.is_active = True
                account.save()
                token = Token.objects.get(user=account).key
                data["username"] = account.username
                data["token"] = token
                statuscode = status.HTTP_200_OK
            else:
                data = serializer.errors
                statuscode = status.HTTP_403_FORBIDDEN
            return Response(data, status=statuscode)

        except IntegrityError as e:
            account = User.objects.get(username='')
            account.delete()
            raise ValidationError({"400": f'{str(e)}'})

        except KeyError as e:
            raise ValidationError({"400": f'Field {str(e)} missing'})
