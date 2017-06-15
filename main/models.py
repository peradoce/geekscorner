from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
# Create your models here.

class UserImage(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    image = ResizedImageField(size=[500, 300], quality=75, upload_to='users_avatar')
