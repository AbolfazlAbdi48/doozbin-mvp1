from django.db import models
from django.contrib.auth.models import AbstractUser

from brand.models import Brand, Asset


# Create your models here.
class User(AbstractUser):
    """
    Abstract User Model.
    """

    def __str__(self):
        return self.username


class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='کاربر')
    balance = models.IntegerField(verbose_name='موجودی')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    update = models.DateTimeField(auto_now=True, verbose_name='آخرین آپدیت')

    class Meta:
        verbose_name = 'کیف پول'
        verbose_name_plural = 'کیف پول ها'

    def __str__(self):
        return f"{self.user} - {self.balance} doozcoin"


class UserScan(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='کاربر')
    coin = models.IntegerField(null=True, blank=True, verbose_name='تعداد کوین')
    description = models.CharField(null=True, blank=True, max_length=255, verbose_name='توضیحات')
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.PROTECT, verbose_name='برند')
    accepted = models.BooleanField(default=True, verbose_name='پذیرفته شده/نشده')
    scanned_img = models.ImageField(upload_to='account/scanned/', null=True, blank=True, verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    update = models.DateTimeField(auto_now=True, verbose_name='آخرین آپدیت')

    class Meta:
        verbose_name = 'اسکن'
        verbose_name_plural = 'اسکن ها'

    def __str__(self):
        return f"{self.user} - {self.accepted}"


class OwnedAsset(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='کاربر')
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, verbose_name='asset')
    price = models.IntegerField(null=True, blank=True, verbose_name='قیمت در زمان خرید')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    update = models.DateTimeField(auto_now=True, verbose_name='آخرین آپدیت')

    def __str__(self):
        return f"{self.user} - {self.asset}"
