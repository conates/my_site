from random import choice
from django.core.urlresolvers import reverse
from backend.models import *
from django.conf import settings


def menu(request):
	menu_principal=WpPosts.objects.all().filter(
		post_status="publish",
		wppostmeta__meta_key="_menu_item_url",
		post_type="nav_menu_item",
		wptermrelationships__term_taxonomy__term__name=settings.NOMBRE_MENU_PRINCIPAL
		).order_by('menu_order')

	#menu = {
	#	'menu': [
	#			{'name': post.post_title, 'url': reverse('home')},
		#		{'name': post.post_title, 'url': reverse('blog')},
	#	]
	#}

	menu = {'menu': []}
	for post in menu_principal:
		menu['menu'].append({'name': post.post_title, 'url': reverse(post.post_name)})

	for item in menu['menu']:
		if request.path == item['url']:
			item['active'] = True
	return menu
