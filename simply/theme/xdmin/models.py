from django.db import models
from django.utils.translation import gettext_lazy as _


class Theme(models.Model):

    name = models.CharField(
            unique=True,
            max_length=50,
            verbose_name=_('name'))

    slug = models.SlugField(
            primary_key=True,
            max_length=100,
            verbose_name=_('slug'))

    active = models.BooleanField(
            verbose_name=_('active'))


    branding_title = models.CharField(
            blank=True,
            max_length=50,
            verbose_name=_('title'))

    branding_title_use = models.BooleanField(
            verbose_name=_('use'))

    branding_bg_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('background color'))

    branding_bg_color_use = models.BooleanField(
            verbose_name=_('use'))

    branding_text_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('text color'))

    branding_text_color_use = models.BooleanField(
            verbose_name=_('use'))

    branding_link_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('link color'))

    branding_link_color_use = models.BooleanField(
            verbose_name=_('use'))

    branding_link_hover_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('link hover color'))

    branding_link_hover_color_use = models.BooleanField(
            verbose_name=_('use'))


    header_bg_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('background color'))

    header_bg_color_use = models.BooleanField(
            verbose_name=_('use'))

    header_text_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('text color'))

    header_text_color_use = models.BooleanField(
            verbose_name=_('use'))

    header_link_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('link color'))

    header_link_color_use = models.BooleanField(
            verbose_name=_('use'))

    header_link_hover_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('link hover color'))

    header_link_hover_color_use = models.BooleanField(
            verbose_name=_('use'))


    breadcrumbs_bg_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('background color'))

    breadcrumbs_bg_color_use = models.BooleanField(
            verbose_name=_('use'))

    breadcrumbs_text_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('text color'))

    breadcrumbs_text_color_use = models.BooleanField(
            verbose_name=_('use'))

    breadcrumbs_link_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('link color'))

    breadcrumbs_link_color_use = models.BooleanField(
            verbose_name=_('use'))

    breadcrumbs_link_hover_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('link hover color'))

    breadcrumbs_link_hover_color_use = models.BooleanField(
            verbose_name=_('use'))


    module_bg_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('background color'))

    module_bg_color_use = models.BooleanField(
            verbose_name=_('use'))

    module_text_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('text color'))

    module_text_color_use = models.BooleanField(
            verbose_name=_('use'))

    module_link_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('link color'))

    module_link_color_use = models.BooleanField(
            verbose_name=_('use'))

    module_link_hover_color = models.CharField(
            blank=True,
            max_length=7,
            verbose_name=_('link hover color'))

    module_link_hover_color_use = models.BooleanField(
            verbose_name=_('use'))

    def __str__(self):
        return self.slug
