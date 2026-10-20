from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^auth/', include('djoser.urls')),
    path('api/', include('recipes_api.urls')),
    path('api/', include('ingredients_api.urls')),
    path('api/', include('tags_api.urls')),
]
