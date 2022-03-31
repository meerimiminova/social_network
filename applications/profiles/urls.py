from django.urls import path
from . import views

from applications.profiles.views import ProfileViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', ProfileViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)

# urlpatterns = [
    # path('profile/', views.ProfileViewSet.as_view()),


    # path('profile-update/<int:pk>/', views.ProfileUpdateView.as_view())
# ]

# profile_detail = ProfileViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })
