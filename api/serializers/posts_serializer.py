from rest_framework import serializers
from api.models.posts import Posts


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        exclude = [
            'created_at', 
            'updated_at',
            ]
