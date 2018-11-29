from . import views

from rest_framework import routers

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('profile', views.ProUserViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('propage', views.PropageViewSet)
router.register('posts', views.PostsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='pro_api')),
] 