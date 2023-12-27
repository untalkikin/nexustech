from django.contrib import admin
from .models import Service, Content, PictureUS, Partner

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class ContentAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class PictureUSAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class PartnersAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(PictureUS, PictureUSAdmin)
admin.site.register(Partner, PartnersAdmin)