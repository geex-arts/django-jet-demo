# encoding: utf-8
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from menu.models import MenuItemCategory, MenuItem
from django.utils.translation import ugettext_lazy as _


class MenuItemAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


class MenuItemCategoryMenuItemsInline(SortableInlineAdminMixin, admin.StackedInline):
    model = MenuItem
    extra = 1
    show_change_link = True


class MenuItemCategoryMenuItemsInline2(SortableInlineAdminMixin, admin.TabularInline):
    model = MenuItem
    extra = 1
    show_change_link = True


class MenuItemCategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (MenuItemCategoryMenuItemsInline,MenuItemCategoryMenuItemsInline2)


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuItemCategory, MenuItemCategoryAdmin)

