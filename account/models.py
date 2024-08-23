from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """
    Abstract User Model.
    """

    def __str__(self):
        return self.get_full_name()
