from django.contrib import admin
from .models import *


# class StockAdmin (admin.TabularInline):
#     model = Stock
#
# class GoodsAdmin (admin.ModelsAdmin):
#
# class ServiceAdmin (admin.ModelsAdmin)
#
# class CondignmentAdmin (admin.ModelsAdmin)
#
# class ConsignmentGoodsAdmin (admin.ModelsAdmin)
#
# class ReleaseToSoldiersAdmin (admin.ModelsAdmin)


admin.site.register(Stock)
admin.site.register(Goods)
admin.site.register(Service)
admin.site.register(Consignment)
admin.site.register(ConsignmentGoods)
admin.site.register(ReleaseToSoldiers)
