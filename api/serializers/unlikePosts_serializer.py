from rest_framework import serializers
from api.models.unlike_posts import PostUnlikes


class UnlikePostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostUnlikes
        exclude = [
            'created_at', 
            'updated_at',
            ]
        