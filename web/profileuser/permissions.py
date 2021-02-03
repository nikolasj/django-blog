from rest_framework import permissions


class IsOwnerProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        :param request: request
        :param view: ProfileViewSet
        :param obj: User
        :return: bool
        """
        # if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
        #     return True

        return request.user == obj
