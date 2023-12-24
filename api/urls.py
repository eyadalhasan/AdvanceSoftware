from django.urls import path, include
from rest_framework.routers import DefaultRouter
from communityReport.views import CommunityReportViewSet
from EducationalResource.views import EducationalResourceViewSet
from enviromentalAlert.views import EnvironmentalAlertViewSet
from openDataAccess.views import OpenDataAccessView
from environmentalData.views import EnvironmentalDataViewSet
from score.views import ScoreViewSet


router = DefaultRouter()
router.register(r"communityReport", CommunityReportViewSet, basename="CommunityReport")
router.register(
    r"educationalResource", EducationalResourceViewSet, basename="educationalResource"
)
router.register(
    r"enviromentalAlert", EnvironmentalAlertViewSet, basename="enviromentalAlert"
)

router.register(
    r"environmentalData", EnvironmentalDataViewSet, basename="environmentalData"
)
router.register(r"score", ScoreViewSet, basename="score")
urlpatterns = [
    path("user/", include("Register.urls")),
    path("open_data_access/", OpenDataAccessView.as_view(), name="open_data_access"),
    path("", include(router.urls)),
]
