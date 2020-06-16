#from django.conf.urls import url
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('crear_flor/', login_required(crearFlor), name = "crear_flor"),
	path('listar_flor/', login_required(listarFlor), name = "listar_flor"),
	path('catal_flor/', login_required(catalFlor), name = "catal_flor"),
	path('editar_flor/<id>/', login_required(editarFlor), name = "editar_flor"),
	path('eliminar_flor/<id>/', login_required(eliminarFlor), name = "eliminar_flor"),
	path('detalle_flor/<id>/', login_required(detalleFlor), name = "detalle_flor"),

	path('listar_pedidos/', login_required(listarPedido), name = "listar_pedidos"),
]
"""urlpatterns = [
	url(r'^$', home, name = "index"),
	url(r'^crear_flor/', crearFlor, name = "crear_flor"),
]"""