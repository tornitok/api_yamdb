from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, getjwtoken, registration

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', registration, name='register'),
    path('v1/auth/token/', getjwtoken, name='token'),
]
