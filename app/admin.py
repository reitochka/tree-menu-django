from django.contrib import admin
from .models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent', 'url',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)

