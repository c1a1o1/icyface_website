from django.conf.urls import patterns, include, url
from django.contrib import admin
import web


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'icyface.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'',include('web.urls'))
)
