from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'lists.views.home_page', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^admin/', include(admin.site.urls)),
                       )
