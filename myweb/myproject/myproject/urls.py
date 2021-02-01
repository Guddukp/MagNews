from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'' , include('main.urls')),
    url(r'' , include('news.urls')),
    url(r'' , include('cat.urls')),
    url(r'' , include('subcat.urls')),
    url(r'' , include('contactform.urls')),
    url(r'' , include('trending.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

