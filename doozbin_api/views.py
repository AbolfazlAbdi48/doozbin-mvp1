from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from brand.models import Asset
from .serializers import ARUserSerializer, AssetSerializer
from account.models import ARUser


# Create your views here.
# @method_decorator(csrf_exempt, name='dispatch')
class ARUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ARUserSerializer(data=request.data)
        if serializer.is_valid():
            ar_user = serializer.save()
            reward = None
            if ar_user.rewards.count() >= 1:
                reward = ar_user.rewards.first()
            else:
                reward = Asset.objects.filter(limit__gte=1).first()
                reward.limit -= 1
                reward.save()
                ar_user.rewards.add(reward)

            reward_serializer = AssetSerializer(reward).data
            return Response(reward_serializer, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
