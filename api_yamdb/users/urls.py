from rest_framework.routers import DefaultRouter

from django.urls import include, path
from users.views import (UserViewSet, registration,
                         getjwtoken)

router = DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', registration, name='register'),
    path('v1/auth/token/', getjwtoken, name='token')
]
