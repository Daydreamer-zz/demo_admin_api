#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from django.db import models


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
