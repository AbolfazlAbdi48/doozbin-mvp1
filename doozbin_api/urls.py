from django.urls import path
from .views import ARUserView

app_name = 'api'
urlpatterns = [
    path('ar-user/', ARUserView.as_view(), name='ar-user')
]
