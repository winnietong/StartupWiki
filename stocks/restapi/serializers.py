from stocks.models import User, Category
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User