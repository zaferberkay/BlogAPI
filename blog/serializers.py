from rest_framework import serializers
from .models import Category,Post

class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        exclude = []



class Post_serializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()

    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    
    
    class Meta:
        model=Post
        exclude=[

        ]