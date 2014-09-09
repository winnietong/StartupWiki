from rest_framework import viewsets

from stocks.restapi.serializers import UserSerializer
from stocks.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer