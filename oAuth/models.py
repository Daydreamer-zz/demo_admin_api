from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from utils.basemodel import BaseModel, SoftDeleteModel


# Create your models here.
class NewUser(AbstractUser):
    role_type = [
        [0, "admin"],
        [1, "user"],
    ]
    roles = models.IntegerField(verbose_name="角色", choices=role_type, default=1)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True, auto_now=True)

    objects = UserManager()

    class Meta:
        swappable = "AUTH_USER_MODEL"


class Books(BaseModel, SoftDeleteModel):
    name = models.CharField(verbose_name="书名", max_length=120)
    author = models.CharField(verbose_name="作者", max_length=30)
