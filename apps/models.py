from django.db.models import Model, CharField, ForeignKey, CASCADE, DateTimeField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

class Product(BaseModel):
    name = CharField(max_length=255)
    description = CharField(max_length=255, null=True, blank=True)
    category = ForeignKey('apps.Category',CASCADE,'products')


class User(Model):
    first_name = CharField(max_length=255)
    username = CharField(max_length=255,unique=True)

