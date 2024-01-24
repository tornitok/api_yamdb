from rest_framework import serializers

from users.models import User


class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'role',
            'email',
            'confirmation_code',
            'first_name',
            'last_name',
            'bio',
        ]

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                {
                    'username':
                    'Нельзя использовать имя me в качестве имени пользователя.'
                },
            )
        return value


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("username", "role", "email",
                  "first_name", "last_name", "bio")
        model = User
        read_only_fields = ('role',)

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                {
                    'username':
                    'Нельзя использовать имя me в качестве имени пользователя.'
                },
            )
        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()
