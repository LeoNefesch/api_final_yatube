from django.shortcuts import get_object_or_404
from posts.models import Follow, Group, Post
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthor
from .serializers import CommentSerial, FollowSerial, GroupSerial, PostSerial


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerial
    permission_classes = [IsAuthor]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Redefinition of POST-method."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerial


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerial
    permission_classes = [IsAuthor]

    def get_queryset(self):
        """Redefinition of GET-method."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        """Redefinition of POST-method."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerial
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
