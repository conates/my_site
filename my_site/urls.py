from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'frontend.views.inicio', name='inicio'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', 'frontend.views.blog', name='blog'),
    url(r'^acerca-de/', 'frontend.views.about', name='about'),
    url(r'^contacto/', 'frontend.views.contacto', name='contacto'),
    url(r'^habilidades/', 'frontend.views.habilidades', name='habilidades'),
    url(r'^portafolio/', 'frontend.views.portafolio', name='portafolio'),
    url(r'^admin/', include(admin.site.urls)),
)