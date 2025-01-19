from rest_framework import serializers
from .models import Category  # Убедитесь, что модель Category существует

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Или перечислите нужные поля
