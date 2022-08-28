from django.contrib import admin
from myapp.models import contactEnquiry
from myapp.models import HackerNews


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('sno', 'name', 'email', 'phone', 'subject', 'message')


admin.site.register(contactEnquiry, ContactAdmin)


class HackerAdmin(admin.ModelAdmin):
    list_display = ('titles', 'remark')


admin.site.register(HackerNews, HackerAdmin)
