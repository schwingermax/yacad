# TODO: Implement movie, person and country model admins


from django.contrib import admin
from .models import Brand, Car, Continent


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('name', 'type', "gearbox")
    pass


admin.site.register(Brand, BrandAdmin)


class CarAdmin(admin.ModelAdmin):
    list_filter = ('gearbox',)
    pass


admin.site.register(Car, CarAdmin)

admin.site.register(Continent)
