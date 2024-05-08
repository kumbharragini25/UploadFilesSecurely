from django.contrib.auth.backends import ModelBackend
from owner.models import Owner
from manager.models import Managers
from users.models import Users
from django.contrib.auth.hashers import check_password

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try to authenticate against the Owner model
        owner = Owner.objects.filter(Username=username).first()
        if owner and owner.check_password(password):
            return owner
        
        # Try to authenticate against the Manager model
        manager = Managers.objects.filter(Username=username).first()
        if manager and manager.check_password(password):
            return manager
        
        # Try to authenticate against the Users model
        user = Users.objects.filter(Username=username).first()
        if user and user.check_password(password):
            return user
        
        # Return None if authentication fails
        return None