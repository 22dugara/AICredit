from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def infoView(request):
	return render(request, 'info.html')
