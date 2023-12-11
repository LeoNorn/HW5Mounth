from django.contrib.auth.models import User
from django.db import models


class UserConfirm(models.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
