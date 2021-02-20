from rest_framework.viewsets import ModelViewSet
from apps.measurements.models import Project, Measurement
from apps.measurements.serializers_v1 import ProjectSerializer, MeasurementSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.prefetch_related('measurements')
    serializer_class = ProjectSerializer


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Measurement.objects.select_related('project')
    serializer_class = MeasurementSerializer
