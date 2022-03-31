from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home_view
from social_network import settings


schema_view = get_schema_view(
   openapi.Info(
      title="social network",
      default_version='v1',
      description="This is social network website",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-view'),
    # path('api/v1/profile/', include('applications.profiles.urls')),
    # path('api/v1/profiles/<int:pk>/', profile_detail, name='profile-detail'),
    path('api/v1/profiles/', include('applications.profiles.urls')),
    path('api/v1/posts/', include('applications.posts.urls')),
    path('api/v1/comment/', include('applications.posts.urls')),
    path('api/v1/relationship/', include('applications.profiles.urls')),
    path('swagger(.json|.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


