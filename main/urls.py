from django.urls import path, re_path
from rest_framework import routers
from .views import PostViewSet, CommentViewSet
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet,'asd')

urlpatterns = [
    re_path(r'^$', schema_view)
]
urlpatterns += router.urls
