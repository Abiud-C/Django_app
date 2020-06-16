from django import forms
from apps.aplication.models import *
from apps.login.models import Usuario

class FlorForm(forms.ModelForm):
	class Meta:
		model = Flor
		fields = [
			'name',
			'desc',
			'types',
			'cost',
			'stock',
			'img',
			#'cliente',
		]
		labels = {
			'name': 'Nombre',
			'desc': 'Descripción',
			'types': 'Tipo',
			'cost': 'Costo',
			'stock': 'Cantidad',
			'img': 'Imagen',
		}
		widgets = {
			'name': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Ejemplo: Amapola, Gardenia, Girasol, Tulipán...',
					'id': 'name'
				}
			),
			'desc': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Ejemplo: Planta silvestre, erecta, tallos color verde claro con cerdas y hojas simples en la base...',
					'id': 'desc'
				}
			),
			'types': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Ejemplo: Tipo 1, tipo 2, tipo 3...',
					'id': 'types'
				}
			),
			'cost': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Ejemplo: $1000',
					'id': 'cost'
				}
			),
			'stock': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Ejemplo: 50',
					'id': 'stock'
				}
			),
        }

class PedidoForm(forms.ModelForm):
	class Meta:
		model = Pedido
		fields = [
			#'ordered',
			'quantity',
			#'fecha',
			#'desc',
			'flor',
		]
		labels = {
			#'ordered': 'Orden',
			'quantity': 'Cantidad',
			#'desc': 'Descripción',
			'flor': 'Producto',
		}
		widgets = {
			'quantity': forms.NumberInput(
				attrs = {
					'id': 'stock',
					'value': '1',
					'min': '1',
					'max': '999'
				}
			),
		}