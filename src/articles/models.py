from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from common.models import TimeStampedModel


User = get_user_model()


class Article(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    description = models.CharField(verbose_name=_("description"), max_length=255)
    body = models.TextField(verbose_name=_("article content"))

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Article")

    def __str__(self):
        return f"{self.author.username}'s {self.title}"
