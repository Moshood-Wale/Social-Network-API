from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from api.lib.response import Response
from rest_framework import status
from api.models.posts import Posts
from api.serializers.posts_serializer import PostsSerializer
from rest_framework.permissions import IsAuthenticated


class ManagePostsViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        posts = Posts.objects.all()
        return posts

    def get_object(self):
        posts = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, posts)
        return posts

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = self.get_serializer(posts, many=True)
        return Response(
            data=dict(budgets=serializer.data, total=len(serializer.data)),
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request, *args, **kwargs):
        posts = self.get_object()
        serializer = self.get_serializer(posts)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        posts = self.get_object()
        user = request.user
        serializer = self.get_serializer(posts, data=request.data, partial="partial")
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=["get"],
        detail=False,
        url_name="get-post",
        url_path="get-post",
    )
    def get_my_post(self, request, pk=None):
        user = request.user
        posts = Posts.objects.filter(user=user)
        serializer = self.get_serializer(posts, many=True)
        return Response(data=dict(posts=serializer.data), status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(
            data={"message": "post deleted successfully"}, status=status.HTTP_200_OK
        )
