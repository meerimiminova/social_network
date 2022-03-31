from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('', PostViewSet)
router.register('', CommentViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
