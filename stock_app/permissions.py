from rest_framework import permissions


class IsConsumerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user.user_group.name)
        return request.user.user_group.name == 'Consumer'


class IsSupplierPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.user_group.name == 'Supplier'
