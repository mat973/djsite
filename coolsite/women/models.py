

from django.db import models
from django.urls import reverse

# Create your models here.
class Women(models.Model):
    title =models.CharField(max_length=255, verbose_name='заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank = True, verbose_name='контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='фотография')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    time_update = models.DateTimeField(auto_now_add=True, verbose_name='вермя обовления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
#
    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='вид деятельности')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_id': self.pk})

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id',]