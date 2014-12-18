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
	return render(request, "index.html", locals())

def categoria(request, categoria_id):
	categorias = Categoria.objects.all()
	cat = get_object_or_404(Categoria, pk=categoria_id)
	enlaces = Enlace.objects.filter(categoria = cat)
	return render(request, "index.html", locals())

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
	return render(request, "form.html", locals())

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
	
from django.views.generic import ListView

class EnlaceListView(ListView):
	model = Enlace
	context_object_name = 'enlaces'
	def get_template_names(self):
		return 'index.html'