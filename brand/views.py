from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from account.models import OwnedAsset, UserWallet
from brand.models import Asset


# Create your views here.
class AssetListView(LoginRequiredMixin, ListView):
    model = Asset
    queryset = Asset.objects.filter(listed=True)
    template_name = 'brand/assets_list.html'


@login_required
def buy_asset_view(request, asset_pk):
    asset = get_object_or_404(Asset, id=asset_pk, limit__gt=0)
    from_post = False
    if request.POST:
        user_wallet, created = UserWallet.objects.get_or_create(user=request.user)
        if user_wallet.balance > asset.price:
            asset.limit -= 1
            asset.save()

            owned = OwnedAsset(
                user=request.user,
                asset=asset,
                price=asset.price
            )
            owned.save()

            user_wallet.balance -= asset.price
            user_wallet.save()

            from_post = True

    context = {
        'asset': asset,
        'from_post': from_post
    }
    return render(request, 'brand/buy_asset.html', context)
