from rest_framework     import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit  own profile  """

    def has_object_permission(self, request, view, obj):
        """ check if the usr is trying to edit his profile  """
        if request.method == permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
