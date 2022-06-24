from api.models.posts import Posts
from api.models.unlike_posts import PostUnlikes
from rest_framework import status
from api.serializers.unlikePosts_serializer import UnlikePostsSerializer
from api.lib.response import Response
from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class UnLikeAPIView(generics.GenericAPIView):
    # serializer_class = LikePostsSerializer
    permission_classes = [IsAuthenticated]


    def post(self,request,pk):
        unlike_user = request.user
        unlike_post = Posts.objects.filter(pk=pk)
        check = PostUnlikes.objects.filter(Q(unlike_user=unlike_user) & Q(unlike_post = unlike_post.last() ))
        
        if(check.exists()):
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message":"Already UnLiked"
                })
        
        new_unlike = PostUnlikes.objects.create(unlike_user=unlike_user, unlike_post=unlike_post.last())
        new_unlike.save()
        serializer = UnlikePostsSerializer(new_unlike)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    