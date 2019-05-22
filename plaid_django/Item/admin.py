from django.contrib import admin
from Item.models import AccessToken, Account
# Register your models here.

class AccessTokenAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)
    list_display  = ('user', 'a', 'itemid')

class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', )
    list_display  = ('account_id', 'user')

admin.site.register(AccessToken, AccessTokenAdmin)
admin.site.register(Account, AccountAdmin)