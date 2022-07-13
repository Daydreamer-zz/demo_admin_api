#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from rest_framework import serializers
from oAuth.models import NewUser, Books


class NewUserSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    class Meta:
        model = NewUser
        fields = ["id", "username", "roles", "email", "last_login", "is_active"]

    def get_roles(self, obj):
        return obj.get_roles_display()


class BooksSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Books
        fields = ["id", "name", "author"]
