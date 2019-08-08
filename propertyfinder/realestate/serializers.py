from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from rest_framework import exceptions

from .models import *
from django.contrib.auth.models import User, Group, Permission

User = get_user_model()

class UserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "last_login", "date_joined")


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'is_staff','groups')


class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    groups = Group.objects.filter(name="Customers")
    # groups_data = validated_data.get('groups')
    # groups = []
    # for group in groups_data:
    #     belongTo = Group.objects.get(name=group)
    #     groups.append(belongTo.id)

    user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
    user.groups.set(groups)
    # for group_data in groups_data:
    #     # group = Group.objects.create(user=user, **group_data)
    #     user.groups.add(group_data)
    return user

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")


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

class RoomRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomRequest
        fields = "__all__"

class LandRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandRequest
        fields = "__all__"

class HouseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseRequest
        fields = "__all__"
