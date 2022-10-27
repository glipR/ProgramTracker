from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="info")

    def __str__(self):
        return f"{self.user.username} Info"
