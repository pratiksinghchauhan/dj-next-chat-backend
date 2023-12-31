from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    """
    API Register new Users
    """
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
