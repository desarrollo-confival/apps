from rest_framework.serializers import ModelSerializer
#from rest_framework import routers, serializers, viewsets
from municipio.models import Municipio

class MunicipioSerializer(ModelSerializer):

    class Meta:
        model = Municipio
        fields = ('codigo_dane', 'departamento')
