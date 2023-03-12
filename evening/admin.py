from django.contrib import admin
from . models import *


class WeaponsAdmin(admin.ModelAdmin):
    list_display = ('weapon_name',
                    'weapon_number', 'soldier_ref', 'weapon_registration')
    list_display_links = ('weapon_number',)
    search_fields = ('weapon_number',),
    # list_filter = ('weapon_type',)


class SoldiersAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name',
                    'fathers_name', 'callsign', 'rank')
    list_display_links = ('surname',)
    search_fields = ('surname', 'callsign')


class AmmoAdmin(admin.ModelAdmin):
    list_display = ('ammo_name', 'caliber', 'ammo_type', 'quantity')


admin.site.register(Soldiers, SoldiersAdmin)
admin.site.register(Weapons, WeaponsAdmin)
admin.site.register(Ammo, AmmoAdmin)
