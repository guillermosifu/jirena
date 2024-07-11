from rest_framework import serializers

from tracking.models import *

class TrackingRegistrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingRegistros
        fields = ['id','glosa1','glosa2','glosa3','glosa4','glosa5','glosa6']