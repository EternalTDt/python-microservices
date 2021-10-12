from rest_framework import serializers
from .models import Product

class ProductSerizlizer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'