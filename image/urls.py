from django.urls import path
from .views import UploadImageViewSet
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('upload/', UploadImageViewSet.as_view(), name='upload_image'),
]