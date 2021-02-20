from rest_framework import serializers
from apps.measurements.models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = 'id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at', 'measurements'


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = 'id', 'value', 'project', 'photo', 'created_at', 'updated_at'
