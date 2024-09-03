import json
import os
import base64
from io import BytesIO
from PIL import Image
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render

from account.models import UserScan, UserWallet
from ultralytics import YOLO
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, 'static', 'models', 'best_detect_digi.pt')
model = YOLO(model_path)


# Create your views here.
@login_required
def scan_page_view(request):
    context = {}
    return render(request, 'core/scan_page.html', context)


# @login_required
def scan_img_view(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    # if is_ajax:
    if request.method == 'POST':
        data = json.loads(request.body)
        image_data = data['image']
        image_data = image_data.split(',')[1]
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        wallet, created = UserWallet.objects.get_or_create(user=request.user)

        image_io = BytesIO()
        image.save(image_io, format='PNG')
        image_file = ContentFile(image_io.getvalue(), 'brand.png')

        scan = UserScan(
            user=request.user,
            coin=0,
            description="first scan",
            accepted=False,
            scanned_img=image_file
        )
        scan.save()

        # results = model(scan.scanned_img.path)
        # detected = False
        # if results:
        #     for result in results:
        #         if result.boxes:
        #             for box in result.boxes:
        #                 if box.conf[0].item() >= 0.7:
        #                     scan.description = f"digikala, conf: {box.conf[0].item()}"
        #                     scan.coin = 25
        #                     scan.accepted = True
        #                     scan.save(update_fields=['description', 'coin', 'accepted'])
        #                     wallet.balance += 25
        #                     wallet.save(update_fields=['balance'])
        #                     detected = True
        #                     break
        #             if detected:
        #                 break

        # results = model(scan.scanned_img.path)
        # detected = any(
        #     box.conf[0].item() >= 0.7 for result in results for box in result.boxes
        # ) if results else False
        #
        # if detected:
        #     highest_conf = max(
        #         box.conf[0].item() for result in results for box in result.boxes if box.conf[0].item() >= 0.7)
        #     scan.description = f"digikala, conf: {highest_conf}"
        #     scan.coin = 25
        #     scan.accepted = True
        #     scan.save(update_fields=['description', 'coin', 'accepted'])
        #     wallet.balance += 25
        #     wallet.save(update_fields=['balance'])

        return JsonResponse({'status': False})
    return JsonResponse({'status': 'Invalid request'}, status=400)
    # return HttpResponseBadRequest('Invalid request')
