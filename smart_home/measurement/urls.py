from django.urls import path
from .views import SensorApiView, MeasurementsApiView

urlpatterns = [
    path('sensor/', SensorApiView.as_view()),
    path('sensor/<int:pk>/', SensorApiView.as_view()),
    path('measurement/', MeasurementsApiView.as_view())
]
