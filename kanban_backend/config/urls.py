from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # API schema + docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # app APIs
    path('api/auth/', include('apps.accounts.urls')),  # регистрация / токены / me
    path('api/projects/', include('apps.projects.urls')),
    path('api/tasks/', include('apps.tasks.urls')),

    # ... далее подключим остальные модули
]
