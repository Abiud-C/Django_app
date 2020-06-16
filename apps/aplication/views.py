from django.shortcuts import render, redirect
from .models import *
from .forms import FlorForm, PedidoForm
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.template import RequestContext

class Inicio(TemplateView):
	template_name = 'index.html'
"""
def home(request):
	return render(request, 'index.html')
"""
def carritoIndex(request):
	pedido = Pedido.objects.count()
	return render(request, 'index.html', pedido)

def crearFlor(request):
	if request.method == 'POST':
		form = FlorForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/aplication/listar_flor')
	else:
		form = FlorForm()
	return render(request, 'aplication/crear_flor.html', {'form':form})

"""class CrearFlor(SuccessMessageMixin, CreateView):
	model = Flor
	form_class = FlorForm
	template_name = 'aplication/crear_flor.html'
	succes_url = reverse_lazy('/aplication/listar_flor.html')"""

def listarFlor(request):
	flor = Flor.objects.all()
	context = {'flor':flor}
	return render(request, 'aplication/listar_flor.html', context)

def listarPedido(request):
	pedido = Pedido.objects.all()
	context = {'pedido':pedido}
	return render(request, 'pedidos/listar_pedidos.html', context)

def catalFlor(request):
	flor = Flor.objects.all()
	context = {'flor':flor}
	return render(request, 'aplication/catal_flor.html', context)

def editarFlor(request, id):
	flor = Flor.objects.get(id = id)
	if request.method == 'GET':
		form = FlorForm(instance = flor)
	else:
		form = FlorForm(request.POST, request.FILES, instance = flor)
		if form.is_valid():
			form.save()
		return redirect('/aplication/listar_flor')
	return render(request, 'aplication/editar_flor.html', {'form':form, 'flor':flor})

def detalleFlor(request, id):
	flor = Flor.objects.get(id = id)
	if request.method == 'POST':
		form = PedidoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/aplication/catal_flor')
	else:
		form = PedidoForm()
	return render(request, 'aplication/detalle_flor.html', {'form':form, 'flor':flor})

def eliminarFlor(request, id):
	flor = Flor.objects.get(id = id)
	if request.method == 'POST':
		flor.delete()
		return redirect('/aplication/listar_flor')
	return render(request, 'aplication/eliminar_flor.html', {'flor':flor})

