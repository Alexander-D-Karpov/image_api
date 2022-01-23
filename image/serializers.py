from rest_flex_fields import FlexFieldsModelSerializer
from .models import Image
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'image', 'date']
