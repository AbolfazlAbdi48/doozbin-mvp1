from django.db import models


# Create your models here.
class Brand(models.Model):
    unique_name = models.CharField(max_length=255, unique=True, verbose_name='برند')
    name = models.CharField(max_length=255, verbose_name='نام نمایشی')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    logo = models.ImageField(null=True, blank=True, upload_to='brand/logo/', verbose_name='لوگو')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    update = models.DateTimeField(auto_now=True, verbose_name='آخرین آپدیت')

    def __str__(self):
        return self.unique_name
