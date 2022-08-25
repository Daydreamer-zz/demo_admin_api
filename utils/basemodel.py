#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from django.db import models
from utils.manager import SoftDeleteManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(verbose_name="是否删除", default=False, blank=False, null=False)
    objects = SoftDeleteManager()

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True