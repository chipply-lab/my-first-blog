"""
Definition of urls for djangogirls.
"""

from django.conf.urls import include, url
from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', djangogirls.views.home, name='home'),
    # url(r'^djangogirls/', include('djangogirls.djangogirls.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/',admin.site.urls),    
    url(r'^',include('blog.urls')),
]