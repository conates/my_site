from django import template
register = template.Library()
from backend.models import *

slider_principal = WpPosts.objects.all().filter(
		post_status="publish",
		post_type="post",
		wptermrelationships__term_taxonomy__term__name="home",
		)
slider_principal.filter(wppostmeta__meta_key__in=["data-icon","data-slice2-scale","data-slice1-scale","data-slice2-rotation","data-slice1-rotation","class",])
slider_principal.order_by("wppostmeta__meta_value")


@register.simple_tag
def get_mi_picture(postId):
	var_custom = WpPostmeta.objects.filter(post_id=postId)[1:2]
	for value in var_custom:
		print value.meta_key
 		return value.meta_value

# @register.simple_tag
# def get_custom_var_rotation_1(postId):
# 	var_custom = WpPostmeta.objects.filter(post_id=postId)[3:4]
# 	for value in var_custom:
# 		return value.meta_value

# @register.simple_tag
# def get_custom_var_rotation_2(postId):
# 	var_custom = WpPostmeta.objects.filter(post_id=postId)[4:5]
# 	for value in var_custom:
# 		return value.meta_value

# @register.simple_tag
# def get_custom_var_scale_1(postId):
# 	var_custom = WpPostmeta.objects.filter(post_id=postId)[5:6]
# 	for value in var_custom:
# 		return value.meta_value

# @register.simple_tag
# def get_custom_var_scale_2(postId):
# 	var_custom = WpPostmeta.objects.filter(post_id=postId)[6:7]
# 	for value in var_custom:
# 		return value.meta_value


# @register.simple_tag
# def get_custom_var_icon(postId):
# 	var_custom = WpPostmeta.objects.filter(post_id=postId)[7:8]
# 	for value in var_custom:
# 		return value.meta_value

# @register.simple_tag
# def get_custom_var_class(postId):
# 	var_custom = WpPostmeta.objects.filter(post_id=postId)[9:10]
# 	for value in var_custom:
# 		return value.meta_value 