from django.urls import path, include

from . import views
from knox import views as knox_views

# rest imports
from rest_framework import routers

# login = views.LoginViewSet.as_view({"post": "login"})

router = routers.DefaultRouter()
# router.register("login", login)
router.register("users", views.UserViewSet)
# router.register("permissions", views.Permissions)
router.register("agents", views.AgentViewSet)
router.register("customers", views.CustomerViewSet)
router.register("houses", views.AllHousesViewSet)
router.register("lands", views.LandViewSet)
router.register("rooms", views.RoomViewSet)
router.register("room_requests", views.RoomRequestViewSet)
router.register("house_requests", views.HouseRequestViewSet)
router.register("land_requests", views.LandRequestViewSet)
router.register("commercial_lands", views.CommercialLandViewSet)
router.register("commercial_houses", views.CommercialHouseViewSet)
router.register("house_images", views.HouseImageViewSet)
router.register('house_images/(?P<id>\d+)', views.HouseImageViewSet)
router.register("room_images", views.RoomImageViewSet)
router.register("land_images", views.LandImageViewSet)

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('auth/register/', views.Register.as_view(), name="register"),
    path("auth/login/", views.Login_View.as_view()),
    path("auth/user/", views.User_View.as_view(), name="user"),
    path("profile/", views.ShowProfile.as_view(), name="profile"),
    path("auth/logout/", knox_views.LogoutView.as_view(), name='knox_logout'),
    path("", include(router.urls)),
]
