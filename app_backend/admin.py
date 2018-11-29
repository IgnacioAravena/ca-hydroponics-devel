from django.contrib import admin
from .models import Farm, History


# TODO: agregar los campos para el admin
class FarmAdmin(admin.ModelAdmin):
    pass


class HistoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Farm, FarmAdmin)
admin.site.register(History, HistoryAdmin)
