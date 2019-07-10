from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth.models import AbstractUser

"""
    ======================status=================
    TRUE - property is available for sale or rent
    FALSE - property ain't available for sale or rent

    ======================verified===============
    TRUE - property authenticity is proved
    FALSE - authenticity of the property is not yet proved
"""

class Agent(models.Model):
    name = models.CharField(max_length=150, unique=True, primary_key=True)
    logo = models.FileField(upload_to="logos/")

    def __str__(self):
        return self.name


class CustomerContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tel = models.CharField(
        max_length=15, help_text="Please use the following format +254 70000000"
    )
    email_address = models.EmailField()

    @property
    def fullname(self):
        return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)


class House(models.Model):
    house_no = models.CharField(max_length=150, unique=True)
    bedrooms = models.PositiveIntegerField()
    sitting_rooms = models.PositiveIntegerField()
    showers = models.PositiveIntegerField()
    fitted_with_cctv = models.BooleanField(default=None)
    agent = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.SET_NULL)
    verified = models.BooleanField(default=False)
    for_sale = models.BooleanField(default=False)
    for_rent = models.BooleanField(default=False)

    def __str__(self):
        return self.house_no


class Land(models.Model):
    plot_no = models.CharField(max_length=150, unique=True)
    size = models.DecimalField(
        max_digits=11, decimal_places=2, help_text="Please enter the size in hectares."
    )
    agent = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.SET_NULL)
    verified = models.BooleanField(default=False)
    for_sale = models.BooleanField()
    for_rent = models.BooleanField()

    def __str__(self):
        return self.plot_no


class Room(models.Model):
    ROOM_TYPES = (("Single", "single bed"), ("Double", "Double bed"))
    lodge = models.CharField(max_length=150, null=True)
    room_no = models.CharField(max_length=150, unique=True)
    shower = models.BooleanField(default=None)
    town = models.CharField(max_length=20)
    suburb = models.CharField(max_length=20)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    agent = models.ForeignKey(Agent, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.lodge + " " + self.room_no


class SaleDetails(models.Model):
    price = models.DecimalField(
        max_digits=11, decimal_places=2, help_text="price in KSH"
    )
    status = models.BooleanField(
        default=True, help_text="if checked the property is available"
    )

    class Meta:
        abstract = True

class CommercialLand(SaleDetails):
    plot_no = models.CharField(max_length=150, unique=True)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Commerial_lands"
        ordering = ["price"]


class CommercialHouse(SaleDetails):
    house_no = models.CharField(max_length=150, unique=True)
    land = models.ForeignKey(House, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Commerial_houses"
        ordering = ["price"]

    def __str__(self):
        return self.name


class Ammenity(models.Model):
    TYPES_OF_AMMENITIES = (
        ("HOSP", "HOSPITAL"),
        ("SCH", "SCHOOL"),
        ("POLICE STN", "POLICE STATION"),
        ("MKT", "MARKET"),
    )
    ammenity_type = models.CharField(
        max_length=10, choices=TYPES_OF_AMMENITIES, default=None
    )
    name = models.CharField(max_length=150)
    distance = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        verbose_name_plural = "Ammenities"

    def __str__(self):
        return self.name


class HouseImage(models.Model):
    house = models.ForeignKey(House, blank=True, null=True, on_delete=models.CASCADE)
    image_url = models.FileField(upload_to="images/", unique=True)


class RoomImage(models.Model):
    Room = models.ForeignKey(Room, blank=True, null=True, on_delete=models.CASCADE)
    image_url = models.FileField(upload_to="images/", unique=True)


class LandImage(models.Model):
    land = models.ForeignKey(Land, blank=True, null=True, on_delete=models.CASCADE)
    image_url = models.FileField(upload_to="images/", unique=True)

