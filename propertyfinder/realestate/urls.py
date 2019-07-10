from django.urls import path, include

from . import views
from knox import views as knox_views

# rest imports
from rest_framework import routers

# login = views.LoginViewSet.as_view({"post": "login"})

router = routers.DefaultRouter()
# router.register("login", login)
router.register("users", views.UserViewSet)
router.register("agents", views.AgentViewSet)
router.register("customers", views.CustomerViewSet)
router.register("houses", views.AllHousesViewSet)
router.register("lands", views.LandViewSet)
router.register("rooms", views.RoomViewSet)
# router.register("houses_for_sale", views.HouseForSaleViewSet)
# router.register("houses_for_rent", views.HouseForRentViewSet)
# router.register("lands_for_sale", views.LandForSaleViewSet)
router.register("commercial_lands", views.CommercialLandViewSet)
router.register("commercial_houses", views.CommercialHouseViewSet)
router.register("house_images", views.HouseImageViewSet)
router.register("room_images", views.RoomImageViewSet)
router.register("land_images", views.LandImageViewSet)

urlpatterns = [
    path("auth/", include("knox.urls")),
    path("auth/register/", views.Register.as_view(), name="register"),
    path("login/", views.Login_View.as_view()),
    path("user/", views.User_View.as_view(), name="user"),
    path("profile/", views.ShowProfile.as_view(), name="profile"),
    path("auth/logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("", include(router.urls)),
]
