from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('test_app.urls')),
    path('member/', include('django.contrib.auth.urls')),
    path('member/', include('members.urls')),
]
