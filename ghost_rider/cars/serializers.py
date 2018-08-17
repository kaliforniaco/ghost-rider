from rest_framework import serializers
from .models import Car, Comment
from django.contrib.auth.models import User

## Block bellow from SO
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())
    class Meta(object):
        model = User
        fields = ('username', 'email','post')
## END Block bellow from SO


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'year', 'img_url')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'car')

