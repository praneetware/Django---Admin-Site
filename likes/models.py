from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class LikedItem(models.Model):
    #What tag applied to what object
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Type (to search table)
    #ID (To search record in table)
    #content_object for reading actual object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
