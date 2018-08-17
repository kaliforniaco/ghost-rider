from rest_framework import serializers
from .models import Car, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'cars')


class CarSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'year', 'description', 'img_url', 'owner', )


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'car')

