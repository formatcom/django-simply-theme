from django import forms
from django.contrib import admin

from simply.theme.xdmin.models import Theme

class ThemeAdminForm(forms.ModelForm):

    SET_FIELDS_COLOR = (
            'branding_bg_color',
            'branding_text_color',
            'branding_link_color',
            'branding_link_hover_color',

            'header_bg_color',
            'header_text_color',
            'header_link_color',
            'header_link_hover_color',

            'breadcrumbs_bg_color',
            'breadcrumbs_text_color',
            'breadcrumbs_link_color',
            'breadcrumbs_link_hover_color',

            'module_bg_color',
            'module_text_color',
            'module_link_color',
            'module_link_hover_color',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        theme = kwargs.get('instance')

        if not theme:
            theme = {}

        for name in self.SET_FIELDS_COLOR:
            self.fields[name].widget = admin.widgets.AdminTextInputWidget(
                    attrs={'type': 'color'}
            )

            self.fields[name].help_text = 'hex: {}'.format(getattr(theme, name, '#000000'))
