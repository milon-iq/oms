from django.db import models
from systems.models import BaseModel


# Create your models here.
class Brand(BaseModel):
    brand_title = models.CharField(max_length=50)

    class Meta:
        db_table = 'brands'


class Category(BaseModel):
    category_title = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'
