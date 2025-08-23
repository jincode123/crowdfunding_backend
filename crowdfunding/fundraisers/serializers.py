from rest_framework import serializers
from django.apps import apps




class FundraiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    
    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'
        

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('fundraisers.Pledge')
        fields = '__all__'

class FundraiserDetailSerializer(serializers.ModelSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'
        depth = 1  # Include related objects in the output

        