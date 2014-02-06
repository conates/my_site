from django.contrib import admin
from models import *
# Register your models here.


class WpPostsAdmin(admin.ModelAdmin):
	list_display=('id','post_title','post_name','post_status','post_modified','post_type','es_popular','comment_count')
	list_filter = ('post_status','post_type',)
	search_fields=('post_title','post_content',)
	list_editable=('post_title','post_status','post_name')




class WpCommentsAdmin(admin.ModelAdmin):
	list_display=('comment_author','comment_content','link_post',)
	list_filter = ('comment_author',)

	def link_post(self, obj):
		objeto=obj.comment_post_id
		id_obj=obj.comment_post_id.id
		cantidad=obj.comment_post_id.comment_count
		tag='<span><a href="/admin/backend/wpposts/%s/" title="%s">%s</a></span><small>%s</small><span><a href="http://localhost/blog/?p=%s/" title="%s" target="_blank">Ver Entrada</a></span>'%(id_obj,objeto,objeto,cantidad,id_obj,objeto)
		return tag
	link_post.allow_tags=True
	link_post.admin_order_field="comment_post_id"


admin.site.register(WpPosts,WpPostsAdmin)
admin.site.register(WpComments,WpCommentsAdmin)