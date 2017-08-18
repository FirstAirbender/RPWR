"""RPWR URL Configuration

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
from django.conf.urls import *
from django.contrib import admin
from information.views import *

information_resource = InformationResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
	url(r'^$', home, name='home'),
	url(r'^add_student/$', add_student, name='add_student'),
	url(r'^details/(?P<form_id>\d+)/$', details, name='details'),
	url(r'^edit/(?P<form_id>\d+)/$', edit_student, name='edit_student'),
    url(r'^api/', include(information_resource.urls)),
    url(r'^welcome/$', welcome, name='welcome'),
    url(r'^error/$', error, name='error'),
]

urlpatterns += [
    url(r'^accounts/login/$', 'cas.views.login', name='login'),
    url(r'^accounts/logout/$', 'cas.views.logout', name='logout'),
]