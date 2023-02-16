from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from places import views


urlpatterns = [
    path('', views.index),
    path('places/<int:place_id>/', views.get_place_json, name="place_json"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
