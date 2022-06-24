from django.contrib import admin
from .models import user, posts, like_posts, unlike_posts


admin.site.register(user.User)
admin.site.register(posts.Posts)
admin.site.register(like_posts.PostLikes)
admin.site.register(unlike_posts.PostUnlikes)
