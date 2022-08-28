from django.urls import path, re_path
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, UserDetail, UserList, RegisterView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Blog API')

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
# router.register(r'comments', CommentViewSet)

urlpatterns = [
    re_path(r'^$', schema_view),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),

]
urlpatterns += router.urls
