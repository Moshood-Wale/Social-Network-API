from api.models.posts import Posts
from api.models.like_posts import PostLikes
from rest_framework import status
from api.serializers.likePosts_serializer import LikePostsSerializer
from api.lib.response import Response
from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class LikeAPIView(generics.GenericAPIView):
    # serializer_class = LikePostsSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request,pk):
        likeusers = request.user
        likepost = Posts.objects.filter(pk=pk)
        check = PostLikes.objects.filter(Q(likeusers=likeusers) & Q(likepost = likepost.last() ))
        
        if(check.exists()):
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message":"Already Liked"
                })
        
        new_like = PostLikes.objects.create(likeusers=likeusers, likepost=likepost.last())
        new_like.save()
        serializer = LikePostsSerializer(new_like)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
