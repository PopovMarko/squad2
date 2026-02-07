from django.db import models
from evening.models import Soldiers
from django.urls import reverse


class Stock(models.Model):
    """
    Model describing leftovers on stock
    """

    goods_ref = models.ForeignKey(
        "goods", on_delete=models.PROTECT, blank=True, null=True, verbose_name="Найменування")
    goods_quantity = models.IntegerField(verbose_name="Кільксть")

    def __str__(self):
        return str(self.goods_ref)

    def get_absolute_url(self):
        return reverse('material-index', kwargs={'pk': self.pk})


class Goods(models.Model):
    """
    Model of  Catalog of goods
    """

    goods_code = models.CharField(
        max_length=50, unique=True, blank=True, null=True, verbose_name="Артикул")
    goods_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Найменування")
    life_time = models.DurationField(default=365, verbose_name="Строк служби")
    goods_unit = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Один. виміру")
    goods_description = models.TextField(max_length=255, verbose_name="Опис")

    def __str__(self):
        return self.goods_name


class Service(models.Model):
    """
    Model of services that supplay goods at stock (catalog)
    """

    service_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Найменування служби")
    service_comm = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Начальник")

    def __str__(self):
        return self.service_name or ''

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'pk': self.pk})


class Consignment(models.Model):
    """
    Model of list of Consignmens from services
    """

    cons_number = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Номер")
    cons_date = models.DateField(
        blank=True, null=True, default="2000-01-01", verbose_name="Дата")
    cons_agent = models.ForeignKey(
        "service", on_delete=models.PROTECT, blank=True, null=True, verbose_name="Служба")
    cons_status = models.BooleanField(
        default=True, verbose_name="Приходна накладна")

    def __str__(self):
        return self.cons_number or ''

    def get_absolute_url(self):
        return reverse("consignment-detail", kwargs={'pk': self.pk})


class ConsignmentGoods(models.Model):
    """
    Model of goods in every consignment
    """

    consignment_ref = models.ForeignKey(
        "consignment", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Накладна"
    )
    goods_ref = models.ForeignKey(
        "goods", on_delete=models.PROTECT, blank=True, null=True, verbose_name="Товар")
    quantity = models.IntegerField(verbose_name="Кількість")

    def get_absolute_url(self):
        return reverse("consignment-detail", args=[str(self.pk)])


class ReleaseToSoldiers(models.Model):
    """
    Model describing release goods to exect soldier
    """

    release_goods = models.ForeignKey(
        "goods", on_delete=models.PROTECT, blank=True, null=True, verbose_name="Товар")
    soldier_ref = models.ForeignKey(
        "evening.soldiers", on_delete=models.PROTECT, blank=True, null=True,
        verbose_name="Військовослужбовець"
    )
    release_date = models.DateField(
        blank=True, null=True, default="2000-01-01", verbose_name="Дата")

    def __str__(self):
        return self.soldier_ref
