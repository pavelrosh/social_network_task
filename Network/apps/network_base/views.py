from rest_framework import viewsets
from . serializers import PostSerializer
from . models import Post
from rest_framework.permissions import IsAuthenticated


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        url = self.request.get_full_path()
        url = url.split('/')
        post_id = self.kwargs['pk']

        post = Post.objects.get(id=post_id)
        if url[-3] == "like":
            post.likes += 1
        elif url[-3] == 'unlike':
            if post.likes > 0:
                post.likes -= 1
        post.save()
        return Post.objects.filter(id=post_id)
