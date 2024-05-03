
from django.contrib import admin

from app.models import Autot, Osat

@admin.register(Osat)
class OsatAdmin(admin.ModelAdmin):
    pass

@admin.register(Autot)
class AutotAdmin(admin.ModelAdmin):
    pass