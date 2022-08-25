from django.db import models
from utils.basemodel import BaseModel, SoftDeleteModel


# Create your models here.
class Books(BaseModel, SoftDeleteModel):
    name = models.CharField(verbose_name="书名", max_length=120)
    author = models.CharField(verbose_name="作者", max_length=30)