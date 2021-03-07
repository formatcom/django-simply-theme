from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class BrandingConfig(AppConfig):
    name = 'simply.theme.branding'
    verbose_name = _("Simply Branding")
