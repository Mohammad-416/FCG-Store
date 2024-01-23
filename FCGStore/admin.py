from django.contrib import admin
from .models import Game


class GamesAdmin(admin.ModelAdmin):
    list_display = (
        "Title",
        "Version",
    )


# Register your models here.
admin.site.register(Game, GamesAdmin)
