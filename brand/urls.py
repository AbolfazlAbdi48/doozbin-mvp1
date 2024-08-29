from django.urls import path
from .views import (
    AssetListView, buy_asset_view
)

app_name = "brand"
urlpatterns = [
    path('shop/', AssetListView.as_view(), name="shop"),
    path('shop/buy/<int:asset_pk>', buy_asset_view, name="buy-asset"),
]
