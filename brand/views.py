from django.shortcuts import render
from django.views.generic import ListView

from brand.models import Asset


# Create your views here.
class AssetListView(ListView):
    """
    TODO: login required
    """
    model = Asset
    template_name = 'brand/assets_list.html'
