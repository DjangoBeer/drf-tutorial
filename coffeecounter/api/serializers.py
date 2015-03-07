from .models import Badge, Consumption, PoweredBadge
from django.contrib.auth.models import User
from rest_framework import serializers

class PoweredBadgeSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='badge.title', read_only=True)
    description = serializers.CharField(source='badge.description', read_only=True)

    class Meta:
        model = PoweredBadge
        fields = ('id', 'title', 'description', 'power')


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ('id', 'title', 'description')


class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumption
        fields = ('id', 'user', 'created')


class UserSerializer(serializers.ModelSerializer):

    badges = PoweredBadgeSerializer(source='poweredbadge_set', many=True)
    twitter = serializers.CharField(source='coffeeuser.twitter')

    class Meta:
        model = User
        fields = ('id', 'username', 'badges', 'twitter')
