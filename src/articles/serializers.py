from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "id",
            "author",
            "title",
            "description",
            "body",
            "created_at",
            "updated_at",
        ]
