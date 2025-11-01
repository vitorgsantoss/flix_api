from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('api/v1/actors/', include('actors.urls')),
    path('api/v1/authentication/', include('authentication.urls')),
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/genres/', include('genres.urls')),
    path('api/v1/reviews/', include('reviews.urls')),
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
