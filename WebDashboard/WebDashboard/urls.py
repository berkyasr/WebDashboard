"""WebDashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from Dashboard import views
urlpatterns = [
    url(r'^$', views.mainpage),
    url(r'^create/$', views.create),

    #mblog pages
    url(r'^insertmblog/$', views.insertmblog),
    url(r'^(?P<id>mblog[0-9]+)/$', views.viewmblog),
    url(r'^likedislike/(?P<id>mblog[0-9]+)/(?P<entry>[0-9]+)/$', views.likedislike),
    url(r'^mbloglist/$', views.mbloglist),

    url(r'^insertweather/$', views.insertweather),

    #poll pages
    url(r'^insertpoll/$', views.insertpoll),
    url(r'^(?P<id>poll[0-9]+)/$', views.viewpoll),
    url(r'^votepoll/(?P<id>poll[0-9]+)/(?P<entry>.+)/$', views.votepoll),
    url(r'^polllist/$', views.polllist),
    
    #gallery
    url(r'^insertgallery/$', views.insertgallery),
    url(r'^(?P<id>gallery[0-9]+)/$', views.viewgallery),
    url(r'^gallerymove/(?P<id>gallery[0-9]+)/$', views.gallerymove),

    url(r'^saveorload/$', views.saveorload),
    url(r'^save/$', views.save),

    url(r'^insertmoneyrate/$', views.insertmoneyrate),
    url(r'^money/$', views.moneys),
    #note pages
    url(r'^insertnote/$', views.insertnote),
    url(r'^notelist/$', views.notelist),
    url(r'^(?P<id>note[0-9]+)/$', views.viewnote),
    url(r'^deleteelement/(?P<id>note[0-9]+)/(?P<element>.+)/$',views.deleteelement),
    
    #clock
    url(r'^clock/$', views.viewclock),
    url(r'^insertclock/$', views.insertclock),
    
    #sticky
     url(r'^insertsticky/$', views.insertsticky),
     url(r'^(?P<id>sticky[0-9]+)/$', views.viewsticky),
     
     url(r'^login/$', views.loginpage),
     url(r'^logout/$', views.logout_view)

]
