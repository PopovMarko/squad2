from django.db import models
from django.urls import reverse
# from django.urls import reverse


class Soldiers(models.Model):
    """
    Поіменний список військовослужбовців підрозділу
    """
    slug = models.SlugField(max_length=50, unique=True, null=True,
                            verbose_name='Код посади')
    surname = models.CharField(max_length=50, verbose_name='Фамілія')
    name = models.CharField(max_length=50, verbose_name='Імʼя')
    fathers_name = models.CharField(max_length=50, verbose_name='По батькові')
    callsign = models.CharField(max_length=50, verbose_name='Позивний')
    position_name = models.CharField(
        max_length=50, null=True, verbose_name='Посада')
    mil_prof = models.CharField(max_length=50, null=True, verbose_name='ВОС')
    position_rank = models.CharField(
        max_length=50, null=True, verbose_name='Звання посади')
    rank = models.ForeignKey(
        'Ranks', on_delete=models.PROTECT, null=True, verbose_name='Звання')
    phone = models.CharField(max_length=13, null=True, verbose_name='Телефон')
    birth_date = models.DateField(null=True, verbose_name='Дата народження')
    tax_number = models.CharField(
        max_length=15, unique=True, null=True, verbose_name='ІПН')
    blood_type = models.CharField(
        max_length=10, null=True, verbose_name='Группа крові')
    addres = models.CharField(max_length=255, null=True, verbose_name='Адреса')

    def __str__(self):
        return f'{self.surname} {self.name}.{self.fathers_name}.'

    def get_absolute_url(self):
        return reverse('soldier', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Військовослужбовець'
        verbose_name_plural = 'Військовослужбовці'
        ordering = ['slug']


# class Staffing(models.Model):
#     """
#     Штатний розклад
#     """
#     slug = models.SlugField(max_length=50, unique=True, null=True,
#                             verbose_name='Код посади')
#     position_name = models.CharField(
#         max_length=50, null=True, verbose_name='Посада')
#     mil_prof = models.CharField(max_length=50, null=True, verbose_name='ВОС')
#     position_rank = models.CharField(
#         max_length=50, null=True, verbose_name='Звання посади')


class Weapons(models.Model):
    """
    Список зброї яка знаходиться в підрозділі
    """
    weapon_name = models.CharField(
        max_length=50, verbose_name='Наіменування зброї')
    weapon_number = models.CharField(
        max_length=50, unique=True, verbose_name='Номер зброї')
    TYPES = (
        ('p', 'Пістолет'),
        ('s', 'Стрілкова зброя'),
        ('m', 'Кулемет ручний'),
        ('mb', 'Кулемет великокаліберний'),
        ('mr', 'Міномет'),
        ('g', 'Гранатомет'),
    )
    weapon_type = models.CharField(
        max_length=50, choices=TYPES, verbose_name='Тип зброї')
    weapon_registration = models.BooleanField(default=True)
    year_manufacture = models.DateField(
        null=True, verbose_name='Рік виготовлення')

    def __str__(self):
        return self.weapon_name

    class Meta:
        verbose_name = 'Зброя підрозділу'
        verbose_name_plural = 'Зброя підрозділу'
        ordering = ['weapon_type', 'weapon_name']


class WeaponCard(models.Model):
    """
    Картка закріпленної зборої за військовослужбовцем 
    """
    soldier = models.ForeignKey(
        'Soldiers', on_delete=models.PROTECT, verbose_name='Військовослужбовець'
    )
    weapon = models.OneToOneField(
        'Weapons', on_delete=models.PROTECT, unique=True,  verbose_name='Закріплена зброя'
    )

    def __str__(self):
        return self.soldier.surname

    class Meta:
        verbose_name = 'Картка зброї військовослужбовця'
        verbose_name_plural = 'Картки зброї військовослужбовців'
        ordering = ['soldier']


class Ranks (models.Model):
    rank = models.CharField(max_length=50,)

    def __str__(self):
        return self.rank
