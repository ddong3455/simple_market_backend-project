from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('seller',)  # seller는 서버에서 자동으로 넣을거라 직접 받지 않음
