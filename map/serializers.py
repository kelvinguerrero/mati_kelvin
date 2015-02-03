__author__ = 'kelvin'
from rest_framework import serializers
from map.models import Pensum
from map.models import Course
from django.contrib.auth.models import User


class PensumSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    pensumName = serializers.HyperlinkedIdentityField(view_name='pensum-highlight', format='html')

    class Meta:
        model = Pensum
        fields = ('name', 'active')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='course-highlight', format='html')

    class Meta:
        model = Course
        fields = ('code', 'credits', 'name', 'summer', 'pensum')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), view_name='user-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'user')