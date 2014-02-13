# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from backend.models import *
from django.conf import settings




# Create your views here.
def inicio(request):

	post_home = WpPosts.objects.all().filter(
			post_status="publish",
			post_type="post",
			wptermrelationships__term_taxonomy__term__name="Home",
			)
	post_home.order_by("wppostmeta__meta_value")

	return TemplateResponse(request, 'home.html', {'post_home': post_home})

def blog(request):
	return redirect(settings.DOMINIO_BLOG)

def about(request):
	post_about = WpPosts.objects.all().filter(
			post_status="publish",
			post_type="post",
			wptermrelationships__term_taxonomy__term__name="About",
			)
	post_about.order_by("wppostmeta__meta_value")

	return TemplateResponse(request, 'about.html',{'post_about':post_about})

def contacto(request):
	return TemplateResponse(request, 'contacto.html')

def habilidades(request):
	return TemplateResponse(request, 'habilidades.html')

def portafolio(request):
	return TemplateResponse(request, 'portafolio.html')