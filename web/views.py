from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
	return render_to_response('web/index.html',{})

def detect(request):
	return render_to_response('web/detect.html',{})