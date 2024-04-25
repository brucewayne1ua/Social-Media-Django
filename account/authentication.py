from django.contrib.auth.models import User

class EmailAuthBackend:
    def authenticate(self, request, username = None, password = None):
        try:
            user = user.objects.get(email=username)
            if user.chek_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None
        
        def get_user(self, user_id):
            try:
                return User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return None