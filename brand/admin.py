from django.contrib import admin

from brand.models import Brand, Asset


# Register your models here.
class AssetInline(admin.TabularInline):
    model = Asset
    extra = 0
    show_change_link = True


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['unique_name', 'name', 'created']

    inlines = [
        AssetInline
    ]


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_filter = ['listed']
