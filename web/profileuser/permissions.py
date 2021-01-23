from rest_framework import permissions


class IsOwnerProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        :param request: request
        :param view: ProfileViewSet
        :param obj: User
        :return: bool
        """

        return request.user == obj
