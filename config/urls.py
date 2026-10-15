from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from jogos.views import JogoViewSet, estatisticas


router = DefaultRouter()
router.register("jogos", JogoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/estatisticas/", estatisticas),
    path("api/", include(router.urls)),
]