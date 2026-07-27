from rest_framework import viewsets
from producto.models import producto
from producto.api.serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset=producto.objects.all()
    serializer_class=ProductoSerializer