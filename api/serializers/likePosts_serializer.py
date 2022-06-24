from rest_framework import serializers
from api.models.like_posts import PostLikes


class LikePostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikes
        exclude = [
            'created_at', 
            'updated_at',
            ]
        