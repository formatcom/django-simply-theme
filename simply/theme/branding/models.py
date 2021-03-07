from django.db import models
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext_lazy as _


class Branding(models.Model):
    name = models.CharField(
            unique=True,
            max_length=50,
            verbose_name=_('name'))

    active = models.BooleanField(
            verbose_name=_('active'))

    logo = models.FileField(
            upload_to="branding/logo/%Y/%m/%d",
            validators=[validate_image_file_extension,])

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'

    def __str__(self):
        return self.name
