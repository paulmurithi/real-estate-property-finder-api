# to be used fo custom viewsets
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from .permissions import *

from .models import (
    Agent,
    CustomerContact,
    House,
    Land,
    Room,
    # HouseForRent,
    # HouseForSale,
    # LandForSale,
    CommercialLand,
    CommercialHouse,
    HouseImage,
    RoomImage,
    LandImage,
    LandRequest,
    RoomRequest,
    HouseRequest
)

# rest imports
from . import serializers

# from rest_framework.authtoken.models import Token
from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from knox.models import AuthToken
from knox.auth import TokenAuthentication


from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Permission


# class Permissions(generics.GenericAPIView):
#     serializer_class = serializers.UserPermissionsSerializer
#     # permission_classes = [IsAuthenticated,]
#     # authentication_classes = [TokenAuthentication,]
#     # group__id = "2"
#     queryset = get_group_permissions(user_obj, obj=None)


class Register(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)
        })


class ShowProfile(APIView):
    authentication_classes = [
        TokenAuthentication,
    ]

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = serializers.UserProfileSerializer(request.user)
        return Response(serializer.data)


class Login_View(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer
    authentication_classes = [BasicAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
        "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)
        })


class User_View(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user


class Logout_View(APIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

    def post(self, request):
        logout(request)
        return Response(status=204)


# agents viewsets


# class LoginViewSet(viewsets.ViewSet):

#     """
#     Api endpoint to authenticate user. provide either:
#     1. token or
#     2. username and password.
#     """

#     @action(detail=False, methods=["post"])
#     def login(self, request):
#         serializer = serializers.LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data["user"]
#         login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#         username = self.request.user.username
#         return Response({"token": token.key, "username": username}, status=200)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class AgentAllHousesViewSet(viewsets.ModelViewSet):

    """ 
    Api endpoint to list all houses registered under a given agent
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = House.objects.all()
    serializer_class = serializers.HouseSerializer

    def get_queryset(self):
        return House.objects.filter(agent=request.user)


class AgentLandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = serializers.LandSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Land.objects.filter(agent=request.user)


class AgentRoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Room.objects.filter(agent=request.user)


# class AgentHouseForRentViewSet(viewsets.ModelViewSet):
#     queryset = HouseForRent.objects.all()
#     serializer_class = serializers.HouseForRentSerializer
#     authentication_classes = [
#         SessionAuthentication,
#         BasicAuthentication,
#         TokenAuthentication,
#     ]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return HouseForRent.objects.filter(agent=request.user)


# class AgentHouseForSaleViewSet(viewsets.ModelViewSet):
#     queryset = HouseForSale.objects.all()
#     serializer_class = serializers.HouseForSaleSerializer
#     authentication_classes = [
#         SessionAuthentication,
#         BasicAuthentication,
#         TokenAuthentication,
#     ]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return HouseForSale.objects.filter(agent=request.user)


# class AgentLandForSaleViewSet(viewsets.ModelViewSet):
#     queryset = LandForSale.objects.all()
#     serializer_class = serializers.LandForSaleSerializer
#     authentication_classes = [
#         SessionAuthentication,
#         BasicAuthentication,
#         TokenAuthentication,
#     ]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return LandForSale.objects.filter(agent=request.user)


class AgentCommercialLandViewSet(viewsets.ModelViewSet):
    queryset = CommercialLand.objects.all()
    serializer_class = serializers.CommercialLandSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CommercialLand.objects.filter(agent=request.user)


class AgentCommercialHouseViewSet(viewsets.ModelViewSet):
    queryset = CommercialHouse.objects.all()
    serializer_class = serializers.CommercialHouseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CommercialHouse.objects.filter(agent=request.user)


class AgentHouseImageViewSet(viewsets.ModelViewSet):
    queryset = HouseImage.objects.all()
    serializer_class = serializers.HouseImageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class AgentRoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = serializers.RoomImageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class AgentLandImageViewSet(viewsets.ModelViewSet):
    queryset = LandImage.objects.all()
    serializer_class = serializers.LandImageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# admin and customer viewsets


class AgentViewSet(viewsets.ModelViewSet):
    """
    Api endpoint to list all agents registered to our site.
    """

    queryset = Agent.objects.all()
    serializer_class = serializers.AgentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # custom queryset
        return Agent.objects.all().filter()


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomerContact.objects.all()
    serializer_class = serializers.CustomerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class AllHousesViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = serializers.HouseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = serializers.LandSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAgent, IsAuthenticatedOrReadOnly]

    def check_permissions(self, request):
        if request.method != "GET":
            for permission in self.get_permissions():
                if not permission.has_permission(request, self):
                    self.permission_denied(
                        request, message=getattr(permission, 'Cannot perfom the action request. Permisssion denied', None)
                    )


# class HouseForRentViewSet(viewsets.ModelViewSet):
#     queryset = HouseForRent.objects.all()
#     serializer_class = serializers.HouseForRentSerializer
#     authentication_classes = [
#         SessionAuthentication,
#         BasicAuthentication,
#         TokenAuthentication,
#     ]
#     permission_classes = [IsAuthenticatedOrReadOnly]


# class HouseForSaleViewSet(viewsets.ModelViewSet):
#     queryset = HouseForSale.objects.all()
#     serializer_class = serializers.HouseForSaleSerializer
#     authentication_classes = [
#         SessionAuthentication,
#         BasicAuthentication,
#         TokenAuthentication,
#     ]
#     permission_classes = [IsAuthenticatedOrReadOnly]


# class LandForSaleViewSet(viewsets.ModelViewSet):
#     queryset = LandForSale.objects.all()
#     serializer_class = serializers.LandForSaleSerializer
#     authentication_classes = [
#         SessionAuthentication,
#         BasicAuthentication,
#         TokenAuthentication,
#     ]
#     permission_classes = [IsAuthenticatedOrReadOnly]


class CommercialLandViewSet(viewsets.ModelViewSet):
    queryset = CommercialLand.objects.all()
    serializer_class = serializers.CommercialLandSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommercialHouseViewSet(viewsets.ModelViewSet):
    queryset = CommercialHouse.objects.all()
    serializer_class = serializers.CommercialHouseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class HouseImageViewSet(viewsets.ModelViewSet):
    queryset = HouseImage.objects.all()
    serializer_class = serializers.HouseImageSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]


class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = serializers.RoomImageSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]


class LandImageViewSet(viewsets.ModelViewSet):
    queryset = LandImage.objects.all()
    serializer_class = serializers.LandImageSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

class LandRequestViewSet(viewsets.ModelViewSet):
    queryset = LandRequest.objects.all()
    serializer_class = serializers.LandRequestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class RoomRequestViewSet(viewsets.ModelViewSet):
    queryset = RoomRequest.objects.all()
    serializer_class = serializers.RoomRequestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class HouseRequestViewSet(viewsets.ModelViewSet):
    queryset = HouseRequest.objects.all()
    serializer_class = serializers.HouseRequestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
