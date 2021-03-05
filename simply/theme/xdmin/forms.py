from django import forms
from django.contrib import admin

from simply.theme.xdmin.models import Theme

class ThemeAdminForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = '__all__'
        widgets = {
                'header_bg_color': admin.widgets.AdminTextInputWidget(
                        attrs={
                            'type': 'color',
                        }),
                'header_text_color': admin.widgets.AdminTextInputWidget(
                        attrs={
                            'type': 'color',
                        }),
                'header_link_color': admin.widgets.AdminTextInputWidget(
                        attrs={
                            'type': 'color',
                        }),
                'header_link_hover_color': admin.widgets.AdminTextInputWidget(
                        attrs={
                            'type': 'color',
                        }),
        }
