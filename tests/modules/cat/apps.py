from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class CatConfig(AppConfig):
    name = 'cat'
    verbose_name = _('animal')
