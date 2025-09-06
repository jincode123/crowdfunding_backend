from rest_framework import serializers
from django.apps import apps




class FundraiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'
        

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.username')

    class Meta:
        model = apps.get_model('fundraisers.Pledge')
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request', None)
        is_admin = False
        if request and hasattr(request, 'user') and request.user.is_authenticated:
            user = request.user
            is_admin = user.is_staff or user.is_superuser or user.user_type == 'admin'
        # Hide supporter username if anonymous is True and user is not admin
        if hasattr(instance, 'anonymous') and getattr(instance, 'anonymous', False) and not is_admin:
            rep['supporter'] = None  # or 'Anonymous' if you prefer
        return rep

class FundraiserDetailSerializer(FundraiserSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class PledgeDetailSerializer(PledgeSerializer):

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.message = validated_data.get('message', instance.message)
        instance.fundraiser = validated_data.get('fundraiser', instance.fundraiser)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.save()
        return instance

class CampaignSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = apps.get_model('fundraisers.Campaign')
        fields = '__all__'