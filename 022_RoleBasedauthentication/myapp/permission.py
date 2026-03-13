from rest_framework import permissions

class IsStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user.role.name)
        return request.user.is_authenticated and request.user.role.name=='student'
    

class IsFaculty(permissions.BasePermission):

    def has_permission(self, request, view):
         print(request.user.role.name)
         return request.user.is_authenticated and request.user.role.name=='faculty'