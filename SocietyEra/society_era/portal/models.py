from msilib.schema import File
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import uuid 
import os
import qrcode
from io import BytesIO
from django.urls import reverse

class reference_id(models.Model):
    user = models.CharField(max_length=150,null=True)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    gendate = models.DateTimeField(auto_now_add=True)
    reference_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    def __str__(self):
        return self.user
    
class Community(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    president = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    
    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(str(self.uuid))
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img_bytes = BytesIO()
        img.save(img_bytes)
        
        
        # if self.qr_code:
        #     if os.path.isfile(self.qr_code.path):
        #         os.remove(self.qr_code.path)
        # self.qr_code.save(f'qrcodes/{self.uuid}.png', File(img_bytes), save=False)
        # super().save()
        
    def get_absolute_url(self):
            return reverse("community_details", args=[str(self.id)])
        
@receiver(pre_delete, sender=Community)
def community_pre_delete(sender, instance, **kwargs):
    if instance.qr_code:
        if os.path.isfile(instance.qr_code.path):
            os.remove(instance.qr_code.path)        
