from rest_framework import serializers

from .models import Product, ProductView

# Serializers for product and product count models
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
        
class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductView
        fields="__all__"