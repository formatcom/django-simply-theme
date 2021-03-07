from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from simply.theme.xdmin.models import Theme
from simply.theme.xdmin.forms import ThemeAdminForm


class ThemeAdmin(admin.ModelAdmin):

    app_module = 'simply.theme'

    form = ThemeAdminForm

    prepopulated_fields = {'slug': ('name',)}

    search_fields = ('name',)
    list_filter = ('active',)

    fieldsets = (
            (None, {
                'fields': ('name', 'slug', 'active',)
            }),
            (_('Branding'), {
                'fields': (
                    ('branding_title', 'branding_title_use',),
                    ('branding_bg_color', 'branding_bg_color_use',),
                    ('branding_text_color', 'branding_text_color_use',),
                    ('branding_link_color', 'branding_link_color_use',),
                    ('branding_link_hover_color', 'branding_link_hover_color_use',),
                )
            }),
            (_('Header'), {
                'fields': (
                    ('header_bg_color', 'header_bg_color_use',),
                    ('header_text_color', 'header_text_color_use',),
                    ('header_link_color', 'header_link_color_use',),
                    ('header_link_hover_color', 'header_link_hover_color_use',),
                )
            }),
            (_('Breadcrumbs'), {
                'fields': (
                    ('breadcrumbs_bg_color', 'breadcrumbs_bg_color_use',),
                    ('breadcrumbs_text_color', 'breadcrumbs_text_color_use',),
                    ('breadcrumbs_link_color', 'breadcrumbs_link_color_use',),
                    ('breadcrumbs_link_hover_color', 'breadcrumbs_link_hover_color_use',),
                )
            }),
            (_('Module'), {
                'fields': (
                    ('module_bg_color', 'module_bg_color_use',),
                    ('module_text_color', 'module_text_color_use',),
                    ('module_link_color', 'module_link_color_use',),
                    ('module_link_hover_color', 'module_link_hover_color_use',),
                )
            }),
    )

    list_display = ('name', 'slug', 'active',)

    def save_model(self, request, obj, form, change):
        Theme.objects.filter(active=True).update(active=False)

        return super().save_model(request, obj, form, change)


admin.site.register(Theme, ThemeAdmin)

