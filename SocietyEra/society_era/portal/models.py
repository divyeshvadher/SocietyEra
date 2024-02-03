from django.db import models
from django.contrib.auth.models import User
import uuid 

class reference_id(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    gendate = models.DateTimeField(auto_now_add=True)
    reference_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    def __str__(self):
        return self.user.username
    
    
