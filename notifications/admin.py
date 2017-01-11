from django.contrib import admin
from notifications.models import Notifications

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']

admin.site.register(Notifications)
