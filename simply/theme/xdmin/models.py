from django.db import models
from django.utils.translation import gettext_lazy as _


class Theme(models.Model):

    name = models.CharField(
            unique=True,
            max_length=100,
            verbose_name=_('name'))

    active = models.BooleanField(
            verbose_name=_('active'))

    header_bg_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('background color'))

    header_text_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('text color'))

    header_link_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('link color'))

    header_link_hover_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('link hover color'))

    def __str__(self):
        return self.name
