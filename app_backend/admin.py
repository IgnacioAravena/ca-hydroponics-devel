from django.contrib import admin
from .models import Seed, Farm, History


class SeedAdmin(admin.ModelAdmin):
    pass


class FarmAdmin(admin.ModelAdmin):
    pass


class HistoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Seed, SeedAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(History, HistoryAdmin)
