from django.contrib import admin
from .models import Service, Content

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class ContentAdmin(admin.ModelAdmin):
    eadonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
admin.site.register(Content, ContentAdmin)