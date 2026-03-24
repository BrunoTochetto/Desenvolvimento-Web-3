from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudanteViewSet, CursoViewSet, MatriculaViewSet



router = DefaultRouter()

router.register(r'estudantes', EstudanteViewSet)
router.register(r'curso', CursoViewSet)
router.register(r'matricula', MatriculaViewSet)

urlpatterns = [
        path('', include(router.urls)),
]
