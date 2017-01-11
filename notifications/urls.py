from django.conf.urls import url
from notifications import views as notifications_views

urlpatterns = [
	url(r'^show/(?P<notification_id>\d+)/$', notifications_views.show_notification),
	url(r'^delete/(?P<notification_id>\d+)/$', notifications_views.delete_notification),
]
