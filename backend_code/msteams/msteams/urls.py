from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    # super user   username: naresh password:8639912308
    path('auth/',include('authentication.urls')),
    path('teams/',include('teams.urls')),
    path('communication/',include('communication.urls'))
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)