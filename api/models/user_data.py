from django.db import models
from jsonfield import JSONField

class UserData(models.Model):
    """This class represents the userdata model."""
    message = JSONField(null=True)
    client_ip = models.GenericIPAddressField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a human readable representation of the model instance."""
        return "{}".format(self.client_ip)