from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import uuid 
from django.urls import reverse


class Community(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    president = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
        
    def get_absolute_url(self):
            return reverse("community_details", args=[str(self.id)])
        
class reference_id(models.Model):
    user = models.CharField(max_length=150,null=True)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    gendate = models.DateTimeField(auto_now_add=True)
    reference_id = models.CharField(max_length=8,unique=True)
    community = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True, blank=True)
    joined_community = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user
    
@receiver(pre_delete, sender=reference_id)
def reference_id_pre_delete(sender, instance, **kwargs):
    instance.joined_community = False
    instance.save()
