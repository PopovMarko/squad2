from django.contrib import admin
from . models import *


class StaffPlanAdmin(admin.ModelAdmin):
    list_display = ('slug', 'position_name', 'mil_prof',
                    'position_rank', 'soldier')
    list_display_links = ('soldier',)
    search_fields = ('soldier',)


class WeaponsAdmin(admin.ModelAdmin):
    list_display = ('weapon_type', 'weapon_name',
                    'weapon_number', 'weapon_registration')
    list_display_links = ('weapon_number',)
    search_fields = ('weapon_number',)


class WeaponCardAdmin(admin.ModelAdmin):
    list_display = ('soldier', 'weapon')


class SoldiersAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name',
                    'fathers_name', 'callsign')
    list_display_links = ('surname',)
    search_fields = ('surname', 'callsign')


admin.site.register(Soldiers, SoldiersAdmin)
admin.site.register(StaffPlan, StaffPlanAdmin)
admin.site.register(Weapons, WeaponsAdmin)
admin.site.register(WeaponCard, WeaponCardAdmin)
