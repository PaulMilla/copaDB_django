"""copaDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static


urlpatterns = []

# In production, our webserver will be hosting media files, thus removing the need for django to do it
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    ]

# url(r'', include('www.urls')) needs to be last because at that point everything else is thrown at www.urls
urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r''       , include('www.urls')),
]

