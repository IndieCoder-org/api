from rest_framework import serializers

from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = get_user_model().objects.create(
            email=validated_data['email'],
            nick_name=validated_data['nick_name']
        )
        user.set_password(validated_data['password'])
        if 'first_name' in validated_data.keys():
            user.first_name = validated_data['first_name']
        if 'last_name' in validated_data.keys():
            user.last_name = validated_data['last_name']
        if 'nick_name' in validated_data.keys():
            user.nick_name = validated_data['nick_name']
        user.save()

        return user

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "nick_name"
        )


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "first_name",
            "last_name"
        )
