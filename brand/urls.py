from django.urls import path
from .views import (
    AssetListView
)

app_name = "brand"
urlpatterns = [
    path('shop/', AssetListView.as_view(), name="shop"),
]
