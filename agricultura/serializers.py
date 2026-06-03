from rest_framework import serializers
from .models import Agricultor, ProductoAgricola

class AgricultorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agricultor
        fields = '__all__'


class ProductoAgricolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoAgricola
        fields = '__all__'