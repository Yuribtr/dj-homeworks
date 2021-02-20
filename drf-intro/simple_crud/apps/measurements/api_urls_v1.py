from rest_framework.routers import DefaultRouter
from apps.measurements.api_view_v1 import ProjectViewSet, MeasurementViewSet

router = DefaultRouter()
router.root_view_name = 'root'
router.register('projects', ProjectViewSet)
router.register('measurements', MeasurementViewSet)
urlpatterns = [] + router.urls
