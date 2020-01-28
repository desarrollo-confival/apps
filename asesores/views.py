from django.shortcuts import render
from rest_framework.views import APIView
import json
from django.http import HttpResponse
from .serializers import MunicipioSerializer
from municipio.models import Municipio
from .forms import AsesoresForm

#================================================
#==> SERIALIZADOR DE MUNICIPIO
class MunicipioAPI(APIView):
    serializer = MunicipioSerializer

    def get(self, request, format=None):
        lista = Municipio.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')

def asesores(request):
    asesores_form = AsesoresForm()
    return render(request, "asesores/asesores.html", {'form': asesores_form})