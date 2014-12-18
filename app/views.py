from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from datetime import datetime
from app.models import *

# Create your views here.

def home(request):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.all()
	return render_to_response("index.html", locals())

def categoria(request, categoria_id):
	categorias = Categoria.objects.all()
	cat = get_object_or_404(Categoria, pk=categoria_id)
	enlaces = Enlace.objects.filter(categoria = cat)
	return render_to_response("index.html", locals())

def add(request):
	return render_to_response('add.html')

def plus(request, enlace_id):
	enlace = get_object_or_404(Enlace, pk=enlace_id)
	enlace.votos += 1
	enlace.save()
	return redirect('/')

def minus(request, enlace_id):
	enlace = get_object_or_404(Enlace, pk=enlace_id)
	enlace.votos -= 1
	enlace.save()
	return redirect('/')
	