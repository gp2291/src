
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from . srializers import UserViewset

# Create your views here.
class UserViewset(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserViewset
    queryset = get_user_model().objects.all()

