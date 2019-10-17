from . models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content', 'likes']

    def create(self, validated_data):
        user = self.context['request'].user
        post = Post.objects.create(**validated_data, user=user)
        return post
