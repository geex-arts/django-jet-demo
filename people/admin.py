# encoding: utf-8
from django.contrib import admin
from jet.admin import CompactInline
from people.models import Company, County, State, City, Address, Person
from django.utils.translation import ugettext_lazy as _


class StateCountiesInline(admin.TabularInline):
    model = County
    extra = 1
    show_change_link = True


class StateCitiesInline(CompactInline):
    model = City
    extra = 1
    show_change_link = True


class StateAdmin(admin.ModelAdmin):
    inlines = (StateCountiesInline, StateCitiesInline)


class CompanyPersonsInline(admin.StackedInline):
    model = Person
    extra = 1
    show_change_link = True
    fields = ('first_name', 'last_name', 'address')


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    inlines = (CompanyPersonsInline,)


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'city',
        'zip',
    )
    search_fields = ('name', 'city', 'zip')
    list_filter = (
        'city',
    )


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'address',
        'company',
        'email',
    )
    list_editable = ('email',)
    list_filter = (
        'address__city',
        'address__city__state',
        'address__city__county',
        'company',
    )
    ordering = ('last_name', 'first_name')
    readonly_fields = ('phone',)
    search_fields = ('last_name', 'first_name', 'address__name', 'company__name', 'email')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'address', 'company')
        }),
        (_('Contacts'), {
            # 'classes': ('',),
            'fields': ('phone', 'email', 'web')
        }),
    )


class CityAdmin(admin.ModelAdmin):
    raw_id_fields = ('state',)



admin.site.register(Company, CompanyAdmin)
admin.site.register(County)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Person, PersonAdmin)

