# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..user_app.models import User


class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="reviews")
    def __str__(self):
        return self.review

