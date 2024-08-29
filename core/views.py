import json
import base64
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

from django.http import JsonResponse
from django.shortcuts import render

from account.models import UserScan


# Create your views here.
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
    image_file = ContentFile(image_io.getvalue(), 'profile.png')

    scan = UserScan(
        user=request.user,
        coin=10,
        description="digikala billboard",
        accepted=True,
        scanned_img=image_file
    )
    scan.save()
    return JsonResponse({'status': 'OK'})
