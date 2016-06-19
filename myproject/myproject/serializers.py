from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        #fields = ('id', 'type', 'status', 'created_at', 'updated_at', 'argument', 'result')

# vim: ai nu et sw=4 sts=4 ts=4 ru
