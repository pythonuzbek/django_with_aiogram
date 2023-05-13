from .models import Category, Product, User
from rest_framework.serializers import ModelSerializer

class CategoryModelSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ProductModelSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'



class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'