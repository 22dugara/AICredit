from django.shortcuts import render
from django.http import HttpResponse
from .models import userdata
# Create your views here.

def creditinputView(request):
	 return render(request, 'creditinput.html')

def compileView(request):
	results= request.POST
	return render(request, 'display.html', {'userdata': results})




	