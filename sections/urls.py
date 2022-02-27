from django.urls import path, re_path, include
from .views import SectionViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', SectionViewset, basename='sections')
urlpatterns = [
    path('<slug:slug>/',SectionViewset.as_view({'get':'retrieve','post':'update'}))
] + router.urls

