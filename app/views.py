from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from datetime import datetime
from app.models import *
from app.forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.order_by("-votos").all()
	return render_to_response("index.html", locals())

def categoria(request, categoria_id):
	categorias = Categoria.objects.all()
	cat = get_object_or_404(Categoria, pk=categoria_id)
	enlaces = Enlace.objects.filter(categoria = cat)
	return render_to_response("index.html", locals())

@login_required
def add(request):
	if request.method == "POST":
		form = EnlaceForm(request.POST)
		if form.is_valid():
			enlace = form.save(commit=False)
			enlace.usuario = request.user
			enlace.save()
			return redirect("/")
	else:
		form = EnlaceForm()
	return render_to_response("form.html", context_instance = RequestContext(request, locals()))

@login_required
def plus(request, enlace_id):
	enlace = get_object_or_404(Enlace, pk=enlace_id)
	enlace.votos += 1
	enlace.save()
	return redirect('/')

@login_required
def minus(request, enlace_id):
	enlace = get_object_or_404(Enlace, pk=enlace_id)
	enlace.votos -= 1
	enlace.save()
	return redirect('/')
	