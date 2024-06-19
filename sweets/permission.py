from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Разрешение на доступ только владельцу объекта или администратору.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff

class IsDeliveryOrAdmin(permissions.BasePermission):
    """
    Разрешение на доступ для пользователей из группы 'Delivery' или администратора.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name='Delivery').exists() or request.user.is_staff
