from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User, Group
from rest_framework import permissions

class OwnerOrReadOnly(BasePermission):
    message = "you must be the owner";
    def has_object_permission(self, request, view, obj):
        return obj.agent==request.user

class Iscustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Customers'):
            return True
        return False


class IsAgent(permissions.BasePermission):
    def has_permission(self, request, view):
        # if request.user and request.user.groups.filter(name='Agents'):
        if request.user and request.user.is_staff==True:
            return True
        return False

def is_in_group(user, group_name):
  try:
    return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
  except Group.DoesNotExist:
    return False

class HasGroupPermission(BasePermission):
  def has_permission(self, request, view):
    required_groups = view.permission_groups.get(view.action)
    if required_groups == None:
    		return False
    elif 'Agent' in required_groups:
        return True
    else:
      return any([is_in_group(request.user, group_name) for group_name in required_groups])


# view.py
# from .permissions import *

# class FooViewSet(viewsets.ModelViewSet)
#   queryset = Foo.objects.all()
#   serializer_class = FooSerializer
#   permission_classes = [HasGroupPermission]
#   permission_groups = {
#     'create': ['Agents'] # Developers can POST
#     'partial_update': ['Agents',],  # Designers and Developers can PATCH
#     'retrieve': ['Customers'], # retrieve can be accessed without credentials (GET 'site.com/api/foo/1')
#     # list returns None and is therefore NOT accessible by anyone (GET 'site.com/api/foo')
#   }