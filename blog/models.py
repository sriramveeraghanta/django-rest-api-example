from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At", blank=True,
        null=True
    )
    modified_at = models.DateTimeField(
        auto_now=True, verbose_name="Last Modified At", blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __unicode__(self):
        return self.title
