from django.db import models
from django.urls import reverse


class Staff(models.Model):
    slug = models.SlugField(max_length=50, unique=True,
                            verbose_name="Код посади")
    position_name = models.CharField(max_length=50, verbose_name="Посада")
    mil_prof = models.CharField(max_length=50, verbose_name="ВОС")
    position_rank = models.CharField(
        max_length=50, verbose_name="Звання посади")
    soldier = models.OneToOneField(
        "Soldiers", on_delete=models.SET_NULL, null=True, blank=True,
        related_name='staff', verbose_name="Військовослужбовець"
    )

    class Meta:
        verbose_name = 'Штатний розклад'
        ordering = ('slug',)

    def __str__(self):
        return self.position_name

    def get_absolute_url(self):
        return reverse("staff-detail", args=[str(self.soldier_id)])


class Soldiers(models.Model):
    """
    Поіменний список військовослужбовців підрозділу
    """

    surname = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Фамілія")
    name = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name="Імʼя")
    fathers_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="По батькові")
    callsign = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Позивний")
    rank = models.ForeignKey(
        "Ranks", on_delete=models.PROTECT, blank=True, null=True, verbose_name="Звання")
    phone = models.CharField(max_length=13, blank=True,
                             null=True, verbose_name="Телефон")
    birth_date = models.DateField(
        blank=True, null=True, default="2000-01-01", verbose_name="Дата народження")
    tax_number = models.CharField(
        max_length=15, unique=True, blank=True, null=True, verbose_name="ІПН")
    blood_type = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Группа крові")
    addres = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Адреса")
    complect_center = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Центр комплектаціі")
    mob_date = models.DateField(
        blank=True, null=True, default="2000-01-01", verbose_name="Дата мобілізаціі")
    children = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Діти")
    hight_s = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Зріст")
    size = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name="Розмір")
    boots_s = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Взуття")
    head_s = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Головний убор")
    photo = models.ImageField(blank=True, null=True, verbose_name="Фото")
    passport = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Паспорт")

    def __str__(self):
        return f"{self.surname}  {self.name}  {self.fathers_name}"

    def get_absolute_url(self):
        return reverse("staff-detail", args=[str(self.pk)])

    class Meta:
        verbose_name = "Військовослужбовець"
        verbose_name_plural = "Військовослужбовці"


class Ranks(models.Model):
    """
    Каталог військових звань
    """
    rank = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.rank


class Weapons(models.Model):
    """
    Список зброї яка знаходиться в підрозділі
    """

    weapon_name = models.CharField(
        max_length=50, verbose_name="Наіменування зброї")
    weapon_number = models.CharField(
        max_length=50, unique=True, verbose_name="Номер зброї")
    weapon_type = models.ForeignKey(
        "WeaponsTypes", on_delete=models.PROTECT, verbose_name="Тип зброї", default=1)
    weapon_registration = models.BooleanField(default=True)
    year_manufacture = models.DateField(
        blank=True, null=True, default="2000-01-01", verbose_name="Рік виготовлення")
    soldier_ref = models.ForeignKey(
        "Soldiers", on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Закріплено"
    )
    # date_ref = models.DateField(null=True, verbose_name='Дата закріплення')

    def __str__(self):
        return self.weapon_name

    def get_absolute_url(self):
        return reverse("weapons_detaile", args=[str(self.pk)])

    class Meta:
        """
        class Meta
        """

        verbose_name = "Зброя підрозділу"
        verbose_name_plural = "Зброя підрозділу"
        ordering = ["weapon_type", "weapon_name"]


class WeaponsTypes(models.Model):
    w_type = models.CharField(max_length=50)

    def __str__(self):
        return self.w_type


class Ammo(models.Model):
    """
    Список боєприпасів підрозділу
    """

    ammo_name = models.CharField(max_length=255, verbose_name="Найменування")
    caliber = models.CharField(max_length=255, verbose_name="Калібр")
    ammo_type = models.CharField(max_length=255, verbose_name="Маркування")
    quantity = models.IntegerField(verbose_name="Кількість")

    class Meta:
        verbose_name = "Боєкомплект підрозділу"
        verbose_name_plural = "Боєкомплект підрозділу"
        ordering = ["quantity"]

    def __str__(self):
        return f"{self.caliber} {self.ammo_type}"
