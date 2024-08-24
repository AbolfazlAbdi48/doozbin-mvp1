import random
import json
import requests

from django.core.cache import cache
from django.conf import settings

api_base_address = settings.SMS_PANEL_BASE_API
panel_originator = settings.SMS_ORIGINATOR
access_key = settings.SMS_PANEL_ACCESS_KEY


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def send_verification_code(code, phone_number) -> bool:
    send_sms_data = {
        "code": "f1mrhsfmwtc3yjl",
        "sender": panel_originator,
        "recipient": phone_number,
        "variable": {
            "verification-code": f"{code}"
        }
    }
    send_sms_req = requests.post(
        url=f"{api_base_address}/sms/pattern/normal/send",
        data=json.dumps(send_sms_data),
        headers={
            'Content-Type': 'application/json',
            'apikey': access_key
        }
    )
    if send_sms_req.json()['status'] == 'OK':
        return True


def send_otp(request, phone):
    otp_code = random.randint(1000, 9999)
    ip = get_client_ip(request)
    cache.set(f"{ip}-for-authentication", phone, settings.EXPIRY_TIME_OTP)
    cache.set(phone, str(otp_code), settings.EXPIRY_TIME_OTP)

    send_verification_code(otp_code, phone)
