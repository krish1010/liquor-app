from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('liquor/', include('liquor_management_system.urls'))
]
