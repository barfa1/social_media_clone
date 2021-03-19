from django.contrib import auth
from django.db import models
# from django.utils import timezone


class UserInfo(auth.models.User, auth.models.PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)
