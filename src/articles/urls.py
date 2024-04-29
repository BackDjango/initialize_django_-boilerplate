from django.urls import path

from . import views


urlpatterns = [
    path("", views.ArticleListCreateView.as_view(), name="article_crate"),
    path("/<uuid:article_id>", views.ArticleRetrieveUpdateDestroyView.as_view(), name="article_retrieve_update_destroy"),
]
