from django.contrib import admin
from portal.models import reference_id, Community
from django.utils.safestring import mark_safe
# Register your models here.
admin.site.register(reference_id)

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'president', 'description', 'qr_code_display')
    
    def qr_code_display(self, obj):
        return mark_safe(f'<a href="#" target="_blank"><img src="#" alt="QR Code" style="width:50px; height:50px;"></a>')
    
    qr_code_display.short_description = 'QR Code'
    
