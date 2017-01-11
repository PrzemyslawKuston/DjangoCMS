"""cms URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from cms import views as cms_views

urlpatterns = [
    url(r'^$', cms_views.index),
    url(r'^articles/', include('articles.urls')),
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^notifications/', include('notifications.urls')),
    url(r'^about/$', cms_views.about),
    url(r'^accounts/login/$', cms_views.login),
    url(r'^accounts/auth/$', cms_views.auth_view),
    url(r'^accounts/logout/$', cms_views.logout),
    url(r'^accounts/loggedin/$', cms_views.loggedin),
    url(r'^accounts/invalid/$', cms_views.invalid_login),

    url(r'^accounts/create_user/$', cms_views.create_user),
    url(r'^accounts/create_user_success/$', cms_views.create_user_success),
    url(r'^admin/', admin.site.urls),
]
