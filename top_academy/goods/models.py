from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, verbose_name='URL_product')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='Products_image/%Y/%m/%d', default='no_image.jpg', blank=True, null=True,
                              verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name='Скидка')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категории')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id',)

    def __str__(self):
        return self.name


