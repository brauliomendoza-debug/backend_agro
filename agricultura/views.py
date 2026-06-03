from rest_framework import viewsets
from .models import Agricultor, ProductoAgricola
from .serializers import AgricultorSerializer, ProductoAgricolaSerializer


class AgricultorViewSet(viewsets.ModelViewSet):
    queryset = Agricultor.objects.all()
    serializer_class = AgricultorSerializer


class ProductoAgricolaViewSet(viewsets.ModelViewSet):
    queryset = ProductoAgricola.objects.all()
    serializer_class = ProductoAgricolaSerializer