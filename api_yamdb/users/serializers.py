import re

from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import exceptions, serializers
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
    )
    email = serializers.EmailField(
        required=True,
        max_length=254,
    )

    def validate_username(self, value):
        if not re.match(r'^[\w.@+-]+\Z', value):
            raise serializers.ValidationError(
                'Имя пользователя может содержать только буквы, '
                'цифры и символы: @/./+/-/_.'
            )
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" не допускается.'
            )
        return value

    def validate(self, value):
        username = value.get('username')
        email = value.get('email')
        existing_user_with_username = User.objects.filter(
            username=username
        ).first()
        existing_user_with_email = User.objects.filter(email=email).first()

        if existing_user_with_username and (
            existing_user_with_username.email != email
        ):
            raise serializers.ValidationError(
                'Пользователь с указанным ' 'username уже зарегистрирован.'
            )

        if existing_user_with_email and (
            existing_user_with_email.username != username
        ):
            raise serializers.ValidationError(
                'Пользователь с указанным ' 'email уже зарегистрирован.'
            )
        return value


class GetJWTSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'confirmation_code', 'token')

    def validate(self, data):
        username = data.get('username')
        confirmation_code = data.get('confirmation_code')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.NotFound('Пользователь не найден.')

        if user.confirmation_code != confirmation_code:
            raise exceptions.ParseError('Неверный код подтверждения.')

        return data

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return str(refresh.access_token)


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UnicodeUsernameValidator()],
        max_length=User._meta.get_field('username').max_length,
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                'Пользователь с указанным ' 'username уже зарегистрирован.'
            )
        return value
