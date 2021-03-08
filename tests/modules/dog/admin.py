from django.contrib import admin

from .models import Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    app_module = "animals"
