# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from backend.models import *
from django.conf import settings




# Create your views here.
def inicio(request):

	slider_principal = WpPosts.objects.all().filter(
			post_status="publish",
			post_type="post",
			wptermrelationships__term_taxonomy__term__name="Slider Principal",
			)
	slider_principal.filter(wppostmeta__meta_key__in=["data-icon","data-slice2-scale","data-slice1-scale","data-slice2-rotation","data-slice1-rotation",])
	slider_principal.order_by("wppostmeta__meta_value")

	return TemplateResponse(request, 'home.html', {'slider_principal': slider_principal})

def blog(request):
	return redirect(settings.DOMINIO_BLOG)

def about(request):
	return TemplateResponse(request, 'about.html')

def contacto(request):
	return TemplateResponse(request, 'contacto.html')

def habilidades(request):
	return TemplateResponse(request, 'habilidades.html')