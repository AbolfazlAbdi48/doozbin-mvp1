from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User, UserWallet, UserScan

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(UserWallet)
admin.site.register(UserScan)
