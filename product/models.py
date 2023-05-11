from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('Category', verbose_name="Ota kategoriyasi",
                               on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(verbose_name="Kategoriya nomi", max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey("Category", verbose_name="Maxsulot kategoriyasi",
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Maxsulot nomi")
    full_name = models.CharField(verbose_name="Maxsulotning to'liq nomi", max_length=255)
    price = models.DecimalField(verbose_name="Maxsulot narxi", max_digits=17, decimal_places=2)
    description = models.TextField(verbose_name="Maxsulot haqida ma'lumot")

    def __str__(self):
        return self.full_name
