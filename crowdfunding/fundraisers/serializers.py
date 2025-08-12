from rest_framework import serializers
from django.apps import apps
from fundraisers.models import Fundraiser
from fundraisers.serializers import FundraiserSerializer



class FundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'

