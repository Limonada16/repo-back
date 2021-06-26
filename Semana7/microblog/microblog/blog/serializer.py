from blog.models import HashTag, Post
from rest_framework import serializers
import re

class HashTagSerializer(serializers.Serializer):
    label = serializers.CharField()

class PostRegexSerializer(serializers.Serializer):
    content = serializers.CharField()
    
    def create(self, validate_date):
        content = validate_date["content"]
        hashTags = re.findall(r'(\#[\w]+)', content)
        post = Post()
        post.content = content
        post.save()

        for item in hashTags:
            hashtag = HashTag.objects.filter(label=item).last()
            if hashtag == None:
                hashtag = HashTag()
                hashtag.label = item
                hashtag.save()
            
            post.hashTags.add(hashtag)
        
        post.save()


        return post 


class PostSaveSerializer(serializers.Serializer):
    content = serializers.CharField()
    hashTags = serializers.ListField()

    def validate_content(self, value):
        if len(value) > 144:
            raise serializers.ValidationError("Max 144 characters")
        return value

    def create(self, validated_data):
            
            post = Post()
            post.content = validated_data["content"]
            post.save()

            for item in validated_data["hashTags"]:
                hashtag = HashTag.objects.filter(label=item).last()
                if hashtag == None:
                    hashtag = HashTag()
                    hashtag.label = item
                    hashtag.save()
                
                post.hashTags.add(hashtag)
            
            post.save()


            return post 


class PostSerializer(serializers.Serializer):
    content = serializers.CharField()
    hashTags = HashTagSerializer(many=True)
    
    

    