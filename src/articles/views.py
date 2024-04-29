from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions

from .models import Article
from .serializers import ArticleSerializer
from .pagination import ArticleCursorPagination
from .permissions import IsOwnerOrReadOnly


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = ArticleCursorPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        article_id = self.kwargs.get('article_id')
        obj = get_object_or_404(Article, id=article_id)
        return obj

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)
