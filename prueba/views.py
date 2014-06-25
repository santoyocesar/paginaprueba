from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime


def home(request):
	menu = 1
	return render_to_response('home.html', {'current_menu': menu})

def news(request):
	menu = 2
	return render_to_response('news.html', {'current_menu': menu})

def about(request):
	menu = 3
	return render_to_response('about.html', {'current_menu': menu})

