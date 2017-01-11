from django.conf.urls import url
from articles import views as articles_views

urlpatterns = [
    url(r'^$', articles_views.articles),
    url(r'^(?P<article_id>\d+)/$', articles_views.article),
    url(r'^(?P<article_id>\d+)/add_comment/$', articles_views.add_comment),
]
