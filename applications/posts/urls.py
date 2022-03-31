from rest_framework.routers import DefaultRouter
from .views import PostViewSet


router = DefaultRouter()
router.register('', PostViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
