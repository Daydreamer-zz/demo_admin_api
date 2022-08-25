#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from rest_framework import serializers
from books.models import Books


class BooksSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Books
        fields = ["id", "name", "author", "created_at", "updated_at"]