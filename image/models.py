from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField


class Image(models.Model):
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
