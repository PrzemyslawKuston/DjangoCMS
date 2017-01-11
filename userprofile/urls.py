from django.conf.urls import url
from userprofile import views as userprofile_views

urlpatterns = [
    url(r'^profile/$', userprofile_views.user_profile),
]
