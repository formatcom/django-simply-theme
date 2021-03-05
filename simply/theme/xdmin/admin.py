from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from simply.theme.xdmin.models import Theme
from simply.theme.xdmin.forms import ThemeAdminForm


class ThemeAdmin(admin.ModelAdmin):

    form = ThemeAdminForm
    list_display = ('name', 'active',)

admin.site.register(Theme, ThemeAdmin)
