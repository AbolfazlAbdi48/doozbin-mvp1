import json
import os
import base64
from io import BytesIO
from PIL import Image
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile

from django.http import JsonResponse
from django.shortcuts import render

from account.models import UserScan
from ultralytics import YOLO
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, 'static', 'models', 'best_detect_digi.pt')
model = YOLO(model_path)


# Create your views here.
@login_required
def scan_page_view(request):
    context = {}
    return render(request, 'core/scan_page.html', context)


def scan_img_view(request):
    """
    TODO: login required
    TODO: check request is ajax
    TODO: add coin to user wallet
    TODO: connect ai model
    """
    data = json.loads(request.body)
    image_data = data['image']
    image_data = image_data.split(',')[1]
    image = Image.open(BytesIO(base64.b64decode(image_data)))

    image_io = BytesIO()
    image.save(image_io, format='PNG')
    image_file = ContentFile(image_io.getvalue(), 'brand.png')

    scan = UserScan(
        user=request.user,
        coin=1,
        description="first scan",
        accepted=False,
        scanned_img=image_file
    )
    scan.save()

    results = model(scan.scanned_img.path)
    detected = False
    if results:
        for result in results:
            if result.boxes:
                for box in result.boxes:
                    if box.conf[0].item() >= 0.7:
                        scan.description = "digikala"
                        scan.coin = 15
                        scan.accepted = True
                        scan.save()
                        detected = True
                        break
                if detected:
                    break

    return JsonResponse({'status': 'OK'})
