from django.contrib import admin
from Request.models import Request, HookCall
# Register your models here.

class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'rid')
    list_display  = ('session', 'event', 'user','status', 'path', 'created_on')

class HookAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', )
    list_display  = ('webhook_type', 'webhook_type', 'actionsTaken', 'created_on',)

admin.site.register(Request, RequestAdmin)
admin.site.register(HookCall, HookAdmin)