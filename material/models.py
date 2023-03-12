from django.db import models
from evening.models import Soldiers


class Stock(models.Model):
    """
    Model describing leftovers on stock
    """

    goods_ref = models.ForeignKey("goods", on_delete=models.PROTECT, blank=True, null=True, verbose_name="Найменування")
    goods_quantity = models.IntegerField(verbose_name="Кільксть")


class Goods(models.Model):
    """
    Model of  Catalog of goods
    """

    goods_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="Артикул")
    goods_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Фамілія")
    life_time = models.DurationField(default=365, verbose_name="Строк служби")
    goods_unit = models.CharField(max_length=50, blank=True, null=True, verbose_name="Служба")
    goods_description = models.TextField(max_length=255, verbose_name="Опис")


class Service(models.Model):
    """
    Model of services that supplay goods at stock (catalog)
    """

    service_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Найменування служби")
    service_comm = models.CharField(max_length=50, blank=True, null=True, verbose_name="Начальник")


class Consignment(models.Model):
    """
    Model of list of Consignmens from services
    """

    cons_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="Номер")
    cons_date = models.DateField(blank=True, null=True, default="2000-01-01", verbose_name="Дата")
    cons_agent = models.ForeignKey("service", on_delete=models.PROTECT, blank=True, null=True, verbose_name="Служба")
    cons_status = models.BooleanField(default=True, verbose_name="Приходна накладна")


class ConsignmentGoods(models.Model):
    """
    Model of goods in every consignment
    """

    consignmen_ref = models.ForeignKey(
        "consignment", on_delete=models.PROTECT, blank=True, null=True, verbose_name="Накладна"
    )
    goods_ref = models.ForeignKey("goods", on_delete=models.PROTECT, blank=True, null=True, verbose_name="Товар")
    quantity = models.IntegerField(verbose_name="Кількість")


class ReleaseToSoldiers(models.Model):
    """
    Model describing release goods to exect soldier
    """

    release_goods = models.ForeignKey("goods", on_delete=models.PROTECT, blank=True, null=True, verbose_name="Товар")
    soldier_ref = models.ForeignKey(
        "evening.soldiers", on_delete=models.PROTECT, blank=True, null=True, verbose_name="Військовослужбовець"
    )
    release_date = models.DateField(blank=True, null=True, default="2000-01-01", verbose_name="Дата")
