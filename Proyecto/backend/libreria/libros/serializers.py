from rest_framework import serializers
from .models import *

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = "__all__"