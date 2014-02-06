# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

Post_Status = (("publish","Publish"),("inherit","Inherit"),("pending","Pending"),("private","Private"),("future","Future"),("draft","Draft"),("trash","Trash"),)

class WpUsermeta(models.Model):
	umeta_id = models.BigIntegerField(primary_key=True)
	user_id = models.BigIntegerField()
	meta_key = models.CharField(max_length=255, blank=True)
	meta_value = models.TextField(blank=True)
	class Meta:
		managed = False
		db_table = 'wp_usermeta'

class WpUsers(models.Model):
	id = models.BigIntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
	user_login = models.CharField(max_length=60)
	user_pass = models.CharField(max_length=64)
	user_nicename = models.CharField(max_length=50)
	user_email = models.CharField(max_length=100)
	user_url = models.CharField(max_length=100)
	user_registered = models.DateTimeField()
	user_activation_key = models.CharField(max_length=60)
	user_status = models.IntegerField()
	display_name = models.CharField(max_length=250)
	class Meta:
		managed = False
		db_table = 'wp_users'
	def __unicode__(self):
		return "%s - %s"%(self.user_nicename,self.user_email)



class WpPosts(models.Model):
	id = models.BigIntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
	post_author = models.BigIntegerField()
	post_date = models.DateTimeField()
	post_date_gmt = models.DateTimeField()
	post_content = models.CharField(max_length=255,)
	post_title = models.CharField(max_length=255)
	post_excerpt = models.CharField(max_length=255)
	post_status = models.CharField(max_length=20, choices=Post_Status)
	comment_status = models.CharField(max_length=20)
	ping_status = models.CharField(max_length=20)
	post_password = models.CharField(max_length=20)
	post_name = models.CharField(max_length=200)
	to_ping = models.CharField(max_length=255)
	pinged = models.CharField(max_length=255)
	post_modified = models.DateTimeField()
	post_modified_gmt = models.DateTimeField()
	post_content_filtered = models.TextField()
	post_parent = models.BigIntegerField()
	guid = models.CharField(max_length=255)
	menu_order = models.IntegerField()
	post_type = models.CharField(max_length=20)
	post_mime_type = models.CharField(max_length=100)
	comment_count = models.BigIntegerField()

	class Meta:
		managed = False
		db_table = 'wp_posts'
		verbose_name_plural = "Articulos"
	def __unicode__(self):
		return self.post_title

	def post_title_link(self):
		return self.post_title
	def es_popular(self):
		return self.comment_count>2

	es_popular.boolean= True

class WpPostmeta(models.Model):
	meta_id = models.BigIntegerField(primary_key=True)
	post =  models.ForeignKey(WpPosts) 
	meta_key = models.CharField(max_length=255, blank=True)
	meta_value = models.TextField(blank=True)
	class Meta:
		managed = False
		db_table = 'wp_postmeta'
	def __unicode__(self):
		return "%s: %s"%(self.meta_key,self.meta_value)

class WpComments(models.Model):
	comment_id = models.BigIntegerField(db_column='comment_ID', primary_key=True) # Field name made lowercase.
	comment_post_id = models.ForeignKey(WpPosts,db_column='comment_post_ID') # Field name made lowercase.
	comment_author = models.TextField()
	comment_author_email = models.CharField(max_length=100)
	comment_author_url = models.CharField(max_length=200)
	comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100) # Field name made lowercase.
	comment_date = models.DateTimeField()
	comment_date_gmt = models.DateTimeField()
	comment_content = models.TextField()
	comment_karma = models.IntegerField()
	comment_approved = models.CharField(max_length=20)
	comment_agent = models.CharField(max_length=255)
	comment_type = models.CharField(max_length=20)
	comment_parent = models.BigIntegerField()
	user = models.ForeignKey(WpUsers)
	class Meta:
		managed = False
		db_table = 'wp_comments'
		verbose_name_plural = "Comentarios"

class WpCommentmeta(models.Model):
	meta_id = models.BigIntegerField(primary_key=True)
	comment_id = models.ForeignKey(WpComments) 
	meta_key = models.CharField(max_length=255, blank=True)
	meta_value = models.TextField(blank=True)
	class Meta:
		managed = False
		db_table = 'wp_commentmeta'


class WpLinks(models.Model):
	link_id = models.BigIntegerField(primary_key=True)
	link_url = models.CharField(max_length=255)
	link_name = models.CharField(max_length=255)
	link_image = models.CharField(max_length=255)
	link_target = models.CharField(max_length=25)
	link_description = models.CharField(max_length=255)
	link_visible = models.CharField(max_length=20)
	link_owner = models.BigIntegerField()
	link_rating = models.IntegerField()
	link_updated = models.DateTimeField()
	link_rel = models.CharField(max_length=255)
	link_notes = models.TextField()
	link_rss = models.CharField(max_length=255)
	class Meta:
		managed = False
		db_table = 'wp_links'

class WpOptions(models.Model):
	option_id = models.BigIntegerField(primary_key=True)
	option_name = models.CharField(unique=True, max_length=64)
	option_value = models.TextField()
	autoload = models.CharField(max_length=20)
	class Meta:
		managed = False
		db_table = 'wp_options'




class WpTerms(models.Model):
	term_id = models.BigIntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	slug = models.CharField(unique=True, max_length=200)
	term_group = models.BigIntegerField()
	class Meta:
		managed = False
		db_table = 'wp_terms'


class WpTermTaxonomy(models.Model):
	term_taxonomy_id = models.BigIntegerField(primary_key=True)
	term = models.ForeignKey(WpTerms)
	taxonomy = models.CharField(max_length=32)
	description = models.TextField()
	parent = models.BigIntegerField()
	count = models.BigIntegerField()
	class Meta:
		managed = False
		db_table = 'wp_term_taxonomy'

class WpTermRelationships(models.Model):
	object = models.ForeignKey(WpPosts)
	term_taxonomy = models.ForeignKey(WpTermTaxonomy)
	term_order = models.IntegerField()
	class Meta:
		managed = False
		db_table = 'wp_term_relationships'





#-------------------------------------BD ORiginal Wordpress-----------------------------------#
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
# from __future__ import unicode_literals

# from django.db import models

# class WpCommentmeta(models.Model):
# 	meta_id = models.BigIntegerField(primary_key=True)
# 	comment_id = models.BigIntegerField()
# 	meta_key = models.CharField(max_length=255, blank=True)
# 	meta_value = models.TextField(blank=True)
# 	class Meta:
# 		managed = False
# 		db_table = 'wp_commentmeta'

# class WpComments(models.Model):
# 	comment_id = models.BigIntegerField(db_column='comment_ID', primary_key=True) # Field name made lowercase.
# 	comment_post_id = models.BigIntegerField(db_column='comment_post_ID') # Field name made lowercase.
# 	comment_author = models.TextField()
# 	comment_author_email = models.CharField(max_length=100)
# 	comment_author_url = models.CharField(max_length=200)
# 	comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100) # Field name made lowercase.
# 	comment_date = models.DateTimeField()
# 	comment_date_gmt = models.DateTimeField()
# 	comment_content = models.TextField()
# 	comment_karma = models.IntegerField()
# 	comment_approved = models.CharField(max_length=20)
# 	comment_agent = models.CharField(max_length=255)
# 	comment_type = models.CharField(max_length=20)
# 	comment_parent = models.BigIntegerField()
# 	user_id = models.BigIntegerField()
# 	class Meta:
# 		managed = False
# 		db_table = 'wp_comments'

# class WpLinks(models.Model):
# 	link_id = models.BigIntegerField(primary_key=True)
# 	link_url = models.CharField(max_length=255)
# 	link_name = models.CharField(max_length=255)
# 	link_image = models.CharField(max_length=255)
# 	link_target = models.CharField(max_length=25)
# 	link_description = models.CharField(max_length=255)
# 	link_visible = models.CharField(max_length=20)
# 	link_owner = models.BigIntegerField()
# 	link_rating = models.IntegerField()
# 	link_updated = models.DateTimeField()
# 	link_rel = models.CharField(max_length=255)
# 	link_notes = models.TextField()
# 	link_rss = models.CharField(max_length=255)
# 	class Meta:
# 		managed = False
# 		db_table = 'wp_links'

# class WpOptions(models.Model):
# 	option_id = models.BigIntegerField(primary_key=True)
# 	option_name = models.CharField(unique=True, max_length=64)
# 	option_value = models.TextField()
# 	autoload = models.CharField(max_length=20)
# 	class Meta:
# 		managed = False
# 		db_table = 'wp_options'

# class WpPostmeta(models.Model):
# 	meta_id = models.BigIntegerField(primary_key=True)
# 	post_id = models.BigIntegerField()
# 	meta_key = models.CharField(max_length=255, blank=True)
# 	meta_value = models.TextField(blank=True)
# 	class Meta:
# 		managed = False
# 		db_table = 'wp_postmeta'

# class WpPosts(models.Model):
# 	id = models.BigIntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
# 	post_author = models.BigIntegerField()
# 	post_date = models.DateTimeField()
# 	post_date_gmt = models.DateTimeField()
# 	post_content = models.TextField()
# 	post_title = models.TextField()
# 	post_excerpt = models.TextField()
# 	post_status = models.CharField(max_length=20)
# 	comment_status = models.CharField(max_length=20)
# 	ping_status = models.CharField(max_length=20)
# 	post_password = models.CharField(max_length=20)
# 	post_name = models.CharField(max_length=200)
# 	to_ping = models.TextField()
# 	pinged = models.TextField()
# 	post_modified = models.DateTimeField()
# 	post_modified_gmt = models.DateTimeField()
# 	post_content_filtered = models.TextField()
# 	post_parent = models.BigIntegerField()
# 	guid = models.CharField(max_length=255)
# 	menu_order = models.IntegerField()
# 	post_type = models.CharField(max_length=20)
# 	post_mime_type = models.CharField(max_length=100)
# 	comment_count = models.BigIntegerField()
# 	class Meta:
# 		managed = False
# 		db_table = 'wp_posts'

# class WpTermRelationships(models.Model):
# 	object_id = models.BigIntegerField()
# 	term_taxonomy_id = models.BigIntegerField()
# 	term_order = models.IntegerField()
# 	class Meta:
# 		managed = False
# 		db_table = 'wp_term_relationships'

# class WpTermTaxonomy(models.Model):
# 	term_taxonomy_id = models.BigIntegerField(primary_key=True)
# 	term_id = models.BigIntegerField()
# 	taxonomy = models.CharField(max_length=32)
# 	description = models.TextField()
# 	parent = models.BigIntegerField()
# 	count = models.BigIntegerField()
# 	class Meta:
# 		managed = False
# 		db_table = 'wp_term_taxonomy'

# class WpTerms(models.Model):
# 	term_id = models.BigIntegerField(primary_key=True)
# 	name = models.CharField(max_length=200)
# 	slug = models.CharField(unique=True, max_length=200)
# 	term_group = models.BigIntegerField()
# 	class Meta:
# 		managed = False
# 		db_table = 'wp_terms'

# class WpUsermeta(models.Model):
# 	umeta_id = models.BigIntegerField(primary_key=True)
# 	user_id = models.BigIntegerField()
# 	meta_key = models.CharField(max_length=255, blank=True)
# 	meta_value = models.TextField(blank=True)
# 	class Meta:
# 		managed = False
# 		db_table = 'wp_usermeta'

# class WpUsers(models.Model):
# 	id = models.BigIntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
# 	user_login = models.CharField(max_length=60)
# 	user_pass = models.CharField(max_length=64)
# 	user_nicename = models.CharField(max_length=50)
# 	user_email = models.CharField(max_length=100)
# 	user_url = models.CharField(max_length=100)
# 	user_registered = models.DateTimeField()
# 	user_activation_key = models.CharField(max_length=60)
# 	user_status = models.IntegerField()
# 	display_name = models.CharField(max_length=250)
# 	class Meta:
# 		managed = False
# 		db_table = 'wp_users'