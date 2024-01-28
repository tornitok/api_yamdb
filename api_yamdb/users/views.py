from django.contrib.auth.tokens import default_token_generator
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response

from users.models import User
from users.permissions import IsAdmin
from users.serializers import (
    GetJWTSerializer,
    RegistrationSerializer,
    UserSerializer,
)
from users.utils import send_confirmation_email


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    http_method_names = ['get', 'post', 'delete', 'patch']
    lookup_field = 'username'
    lookup_value_regex = r'[\w\@\.\+\-]+'

    @action(
        methods=['GET'],
        detail=False,
        permission_classes=(permissions.IsAuthenticated,),
        url_path='me',
    )
    def get_current_user_info(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @get_current_user_info.mapping.patch
    def update_current_user_info(self, request):
        serializer = UserSerializer(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['role'] = request.user.role
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def getjwtoken(request):
    serializer = GetJWTSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = {'token': serializer.validated_data['token']}
        return Response(data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def registration(request):
    serializer = RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user, created = User.objects.get_or_create(
        **serializer.validated_data,
    )
    token = default_token_generator.make_token(user)
    user.confirmation_code = token
    user.save()
    send_confirmation_email(user.email, token)
    return Response(request.data, status=status.HTTP_200_OK)
