from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from rest_framework import exceptions

from .models import *
from django.contrib.auth.models import User

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "last_login", "date_joined")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ["id", "username", "email"]
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # user = authenticate(**data)
        # if user and user.is_active:
        #     return user
        # raise serializers.ValidationError("invalid credentials.")
        username = data.get("username", "")
        password = data.get("password", "")
        if username and password:
            user = authenticate(**data)
            if user:
                if user.is_active:
                    user = authenticate(**data)
                else:
                    raise exceptions.ValidationError("The user is deactivated.")
            else:
                raise exceptions.ValidationError(
                    "Unable to login with given credentials."
                )
        else:
            raise exceptions.ValidationError(
                "Please provide both username and password."
            )
        return user


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = "__all__"


class HouseSerializer(serializers.ModelSerializer):
    # agent = AgentSerializer()

    class Meta:
        model = House
        fields = "__all__"

    def validate_bedrooms(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "The number of bedrooms cannot be less than zero"
            )
        return value

    def validate_sitting_rooms(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "The number of sitting rooms cannot be less than zero"
            )
        return value

    def validate_showers(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "The number of showers cannot be less than zero"
            )
        return value
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "The price cannot be less than zero"
            )
        return value


class LandSerializer(serializers.ModelSerializer):
    # agent = AgentSerializer()

    class Meta:
        model = Land
        fields = "__all__"

    def validate_size(self, value):
        if value < 0:
            raise serializers.ValidationError("input cannot be less than zero")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "The price cannot be less than zero"
            )
        return value


class RoomSerializer(serializers.ModelSerializer):
    # agent = AgentSerializer()

    class Meta:
        model = Room
        fields = "__all__"

    def validate_beds(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "The number of beds cannot be less than zero"
            )
        return value

    def validate_showers(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "The number of showers cannot be less than zero"
            )
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "The price cannot be less than zero"
            )
        return value


class CommercialLandSerializer(serializers.ModelSerializer):
    land = LandSerializer()

    class Meta:
        model = CommercialLand
        fields = "__all__"

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("The price cannot be less than zero")
        return value


class CommercialHouseSerializer(serializers.ModelSerializer):
    # land = LandSerializer()

    class Meta:
        model = CommercialHouse
        fields = "__all__"

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("The price cannot be less than zero")
        return value


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerContact
        fields = "__all__"


class AmmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ammenity
        fields = "__all__"

    def validate_distance(self, value):
        if value < 0:
            raise serializers.ValidationError("The distance cannot be less than zero")
        return value


class HouseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImage
        fields = "__all__"


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = "__all__"


class LandImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandImage
        fields = "__all__"
