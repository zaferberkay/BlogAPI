from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Category,
    Category_serializer,
    Post,
    Post_serializer,
)

class Category_view(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class=Category_serializer


class Post_view(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class=Post_serializer