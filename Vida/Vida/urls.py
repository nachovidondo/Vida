from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.decorators import login_required
from Members.views import Login, logoutUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Members.urls')),
    path('', include('HomeApp.urls')),
    path('login/', Login.as_view(), name="login"),
    path('logout/', login_required(logoutUsuario), name="logout"),
    
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)