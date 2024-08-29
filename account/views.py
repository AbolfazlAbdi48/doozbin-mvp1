from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView

from account.forms import PhoneNumberForm, VerifyOtpForm, RegisterForm
from account.models import User, OwnedAsset
from extensions.utils import get_client_ip, send_otp


# Create your views here.
def login_view(request):
    form = PhoneNumberForm(request.POST or None)
    ip = get_client_ip(request)
    next_url = request.GET.get('next')

    if next_url:
        cache.set(f"{ip}-for-next-url", next_url, 500)

    if form.is_valid():
        phone_number = form.cleaned_data.get('phone_number')
        send_otp(request, phone_number)
        return redirect('account:otp-verify')

    context = {
        'form': form
    }
    return render(request, 'account/phone_auth.html', context)


def verify_otp_view(request):
    form = VerifyOtpForm(request.POST or None)

    ip = get_client_ip(request)
    phone = cache.get(f"{ip}-for-authentication")
    otp = cache.get(phone)
    next_url = cache.get(f"{ip}-for-next-url")

    if phone is None:
        raise Http404

    if form.is_valid():
        received_code = form.cleaned_data.get('code')

        if otp is not None:
            if otp == received_code:
                user, created = User.objects.get_or_create(username=phone)
                cache.delete(phone)
                cache.delete(f"{ip}-for-authentication")

                if created:
                    login(request, user=user)
                    return redirect('account:complete-register')
                else:
                    login(request, user=user)
                    if next_url:
                        return redirect(next_url)
                    return redirect('core:home')
            else:
                messages.error(request, 'کد تائید اشتباه وارد شده است.')
        else:
            messages.error(request, 'کد تائید منقضی شده.')

    context = {
        'form': form,
        'phone': phone
    }
    return render(request, 'account/verify_otp.html', context)


def complete_register_view(request):
    form = RegisterForm(request.POST or None)
    ip = get_client_ip(request)
    next_url = cache.get(f"{ip}-for-next-url")

    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        raise Http404

    if form.is_valid():
        cd = form.cleaned_data  # cleaned data

        user.first_name = cd.get('first_name')
        # TODO: save referral code
        user.set_unusable_password()
        user.save()

        login(request, user)
        if next_url:
            return redirect(next_url)
        return redirect('core:home')

    context = {
        'form': form
    }
    return render(request, 'account/complete_register.html', context)


@login_required
def user_profile_view(request):
    """
    TODO: login required
    """
    return render(request, 'account/profile.html')


class UserAssetListView(LoginRequiredMixin, ListView):
    model = OwnedAsset
    template_name = 'account/owned_asset.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('-created')
