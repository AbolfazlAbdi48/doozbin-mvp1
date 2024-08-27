from django.urls import path
from .views import (
    scan_page_view,
    scan_img_view,
)

app_name = 'core'
urlpatterns = [
    path('', scan_page_view, name='home'),
    path('scan/img/', scan_img_view, name='scan-img'),
]
