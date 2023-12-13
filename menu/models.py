from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Matn")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="photo")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="vaqt")
    time_update = models.DateTimeField(auto_now=True, verbose_name="o'zgargan vaqt")
    is_published = models.BooleanField(default=True, verbose_name="tahrir")
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="category")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="name")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class About(models.Model):
    title = models.CharField(max_length=300, verbose_name='Sarlavha')
    content = models.TextField(verbose_name="Matn")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="photo")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="vaqt")
    time_update = models.DateTimeField(auto_now=True, verbose_name="o'zgargan vaqt")

    def __str__(self):
        return self.title

