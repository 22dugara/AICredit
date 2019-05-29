from django.shortcuts import render
from django.http import HttpResponse
from .models import machinelearn
import keras
import tensorflow as tf
graph = tf.get_default_graph()
# Create your views here.

def creditinputView(request):
	return render(request, 'creditinput.html')

def compileView(request):
	results= request.POST['name']
	global graph
	with graph.as_default():
		return render(request, 'display.html', {'userdata': machinelearn(request.POST['amountofmoney'], request.POST['term'],request.POST['interest rate'], request.POST['installment'], request.POST['home'], request.POST['income'])})