from django.db import models
from .user import User
from .posts import Posts


class PostLikes(models.Model):
    ''' like post '''

    like_post = models.OneToOneField(Posts, related_name="likes", on_delete=models.CASCADE)
    user_id = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.posts)
