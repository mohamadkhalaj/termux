from django.contrib import admin
from .models import call_log, sms_list, clipboard, contact_list, Token

# Register your models here.


class SMS(admin.ModelAdmin):

    list_display = ('phone_number', 'received', 'read', 'body','user')
    list_filter = ('phone_number', 'received', 'read','user')

    fieldsets = (
        ('Info', {
            'fields' : ('phone_number', 'received', 'read',),
        }),
        ('Body', {
            'fields' : ('body',),
        }),
        ("User", {
            'fields': ('user',),
        }),
    )

class CONTACT(admin.ModelAdmin):

    list_display = ('name', 'phone_number','user')
    list_filter = ('phone_number',)

class CLIPBOARD(admin.ModelAdmin):

    list_display = ('text','user')

class TOKEN(admin.ModelAdmin):

    list_display = ('token','user')


class CALL(admin.ModelAdmin):

    list_display = ('phone_number', 'type', 'date', 'duration','user')
    list_filter = ('date', 'type', 'phone_number', 'user')
    fieldsets = (
        ("info", {
            'fields' : ('phone_number', 'type', 'date', 'duration',),
        }),
        ("User", {
            'fields' : ('user',),
        }),
    )

admin.site.register(sms_list, SMS)
admin.site.register(call_log, CALL)
admin.site.register(clipboard, CLIPBOARD)
admin.site.register(contact_list, CONTACT)
admin.site.register(Token, TOKEN)
