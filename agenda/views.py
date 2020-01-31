from django.shortcuts import render, HttpResponse
#from .models import Calendar 

def agenda(request):
    #calendario = Calendar.objects.all()
    return render(request, "agenda/agenda.html")#, {'calendario':calendario})
