
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSellerOrAdminOrReadOnly(BasePermission):
    
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return request.user.group.filter(name = "Seller").existS()
        