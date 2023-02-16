from django.contrib import admin
from . models import *
# Register your models here.

class StaffPlanAdmin(admin.ModelAdmin):
    list_display = ('slug', 'position_name', 'mil_prof', 'position_rank', 'soldier')
    list_display_links = ('soldier',)
    search_fields = ('soldier',)


class WeaponsAdmin(admin.ModelAdmin):
    list_display = ('weapon_type', 'weapon_name', 'weapon_number', 'weapon_registration')
    list_display_links = ('weapon_number',)
    search_fields = ('weapon_number',)
    

class WeaponCardAdmin(admin.ModelAdmin):
    list_display = ('soldier', 'weapon')


admin.site.register(Soldiers)
admin.site.register(StaffPlan, StaffPlanAdmin)
admin.site.register(Weapons, WeaponsAdmin)
admin.site.register(WeaponCard, WeaponCardAdmin)
