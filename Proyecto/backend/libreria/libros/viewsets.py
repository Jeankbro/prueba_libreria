from rest_framework import viewsets
from .models import *
from .serializers import *

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer