from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('forms/', include('forms.urls')),
    path('guess/', include('guess.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
