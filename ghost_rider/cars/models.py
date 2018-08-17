from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(max_length=100)
    img_url = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.make
    
class Comment(models.Model):
    comment = models.CharField(max_length=280)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment
