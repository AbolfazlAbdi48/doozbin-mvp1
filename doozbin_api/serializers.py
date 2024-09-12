from rest_framework import serializers
from account.models import ARUser
from brand.models import Asset


class ARUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ARUser
        fields = ['user_mobile_id', 'phone_number']

    def create(self, validated_data):
        ar_user, created = ARUser.objects.get_or_create(
            user_mobile_id=validated_data['user_mobile_id'],
            defaults={'phone_number': validated_data['phone_number']}
        )
        return ar_user


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['title', 'value', 'description']
