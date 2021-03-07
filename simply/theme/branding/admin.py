from django.contrib import admin

from simply.theme.branding.models import Branding


class BrandingAdmin(admin.ModelAdmin):

    app_module = 'simply.theme'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

    def save_model(self, request, obj, form, change):
        Branding.objects.filter(active=True).update(active=False)

        return super().save_model(request, obj, form, change)

admin.site.register(Branding, BrandingAdmin)

