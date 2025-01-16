from rest_framework.exceptions import PermissionDenied

class UserGroupPermissionMixin:
    required_groups = []

    def get_permissions(self):
    
        permissions = super().get_permissions()
        
        if not self.request.user.groups.filter(name__in=self.required_groups).exists():
            raise PermissionDenied("You are not authorised")
        
        return permissions
