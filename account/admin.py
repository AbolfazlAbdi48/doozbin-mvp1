from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User, UserWallet, UserScan, OwnedAsset, ARUser


# Register your models here.
class UserWalletInline(admin.TabularInline):
    model = UserWallet
    extra = 0
    show_change_link = True


class UserScanInline(admin.TabularInline):
    model = UserScan
    extra = 0
    show_change_link = True


class OwnedAssetInline(admin.TabularInline):
    model = OwnedAsset
    extra = 0
    show_change_link = True


class CustomUserAdmin(UserAdmin):
    inlines = [
        UserScanInline,
        UserWalletInline,
        OwnedAssetInline
    ]


admin.site.register(User, CustomUserAdmin)


@admin.register(UserWallet)
class UserWalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance', 'created']
    search_fields = ('user__username',)


@admin.register(UserScan)
class UserScanAdmin(admin.ModelAdmin):
    list_display = ['user', 'coin', 'brand', 'accepted', 'created']
    search_fields = ('brand__unique_name', 'brand__name', 'user__username')
    list_filter = ('accepted',)


@admin.register(OwnedAsset)
class OwnedAssetAdmin(admin.ModelAdmin):
    pass


@admin.register(ARUser)
class ARUserAdmin(admin.ModelAdmin):
    pass
