from django.contrib import admin
from Request.models import Request, HookCall
# Register your models here.

class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'rid')
    list_display  = ('session', 'event', 'user','status', 'path', 'created_on')

admin.site.register(Request, RequestAdmin)
admin.site.register(HookCall)