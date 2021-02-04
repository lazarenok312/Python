from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    body = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Subcategory(models.Model):
	name = models.CharField(max_length=200, verbose_name='Название')
	body = models.CharField(max_length=1000)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

	class Meta:
		verbose_name = 'Подкатегория'
		verbose_name_plural = 'Подкатегории'

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200, verbose_name='Название')
	description = models.CharField(max_length=2000, verbose_name='Описание')
	subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
	price = models.FloatField(default=0, verbose_name='Цена')
	body = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='Категория/%Y/%m/%d', blank=True)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'

	def __str__(self):
		return self.name