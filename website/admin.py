from django.contrib import admin
from website import models
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'email', 'message')
    date_hierarchy = 'created_date'


admin.site.register(models.Contact, ContactAdmin)