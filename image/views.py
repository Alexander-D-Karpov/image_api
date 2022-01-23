from rest_framework import generics

from .serializers import ImageSerializer
from .models import Image
from rest_flex_fields.views import FlexFieldsModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class ImageViewSet(FlexFieldsModelViewSet):
    allowed_methods = ["GET"]
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [AllowAny]


class UploadImageViewSet(generics.CreateAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [IsAdminUser]