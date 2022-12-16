from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
        ]
        extra_kwargs = {
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ],
                "required": True,
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This field must be unique.",
                    )
                ],
                "required": True,
            },
            "password": {"write_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def perform_update(self, instance: User, validated_data: dict) -> User:

        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

            setattr(instance, key, value)

        instance.save()

        return instance
