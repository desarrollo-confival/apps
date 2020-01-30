from django.shortcuts import render
from django.http import HttpResponse
from municipio.models import Municipio
from .forms import AsesoresForm


def asesores(request):
    asesores_form = AsesoresForm()
    return render(request, "asesores/asesores.html", {'form': asesores_form})