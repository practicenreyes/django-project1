from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView
from app.views import EnlaceListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mejorandola1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
    url(r'^plus/(\d+)$', 'app.views.plus', name='plus'),
    url(r'^minus/(\d+)$', 'app.views.minus', name='minus'),
    url(r'^add/$', 'app.views.add', name='add'),
    url(r'^categoria/(\d+)$', 'app.views.categoria', name='categoria'),
    url(r'^$', 'app.views.home', name='home'),

    url(r'^about/$', TemplateView.as_view(template_name="index.html"), name='about'),
    url(r'^enlaces/$', EnlaceListView.as_view(), name='enlaces'),

    url(r'^admin/', include(admin.site.urls)),
)
