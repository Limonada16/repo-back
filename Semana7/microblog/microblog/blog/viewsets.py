from django.http import response
from rest_framework import serializers, viewsets
from blog.models import Post
from blog.serializer import PostSaveSerializer, PostSerializer
from rest_framework.response import Response
import io
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class tokenizer(viewsets.ViewSet):
    def get_token(self, request):
        data = request.data
        try:    
            user = User.objects.get(username= data['user'])
            if user.check_password(data['password']):
                token = Token.objects.get(user=user)
                token = Token.objects.create(user=user)
                return Response({
                    "token": token.key
                })
            else:
                return Response({
                    "status": "unauthorized"
                })
        except:
            return Response({
                "status": "unauthorized"
            })


class PostViewset(viewsets.ViewSet):
    #authentication_classes = [BasicAuthentication, ]
    #permission_classes = [IsAuthenticated]


    def retrieve(self, request, id):
        queryset = Post.objects.get(pk=id)
        serializer = PostSerializer(queryset)
        return Response(serializer.data)

    def list(self, request):
        status = False
        posts = []
        queryset = Post.objects.all()
        for item in queryset:
            serialized = PostSerializer(item)
            posts.append(serialized.data)

        if queryset != None:
            status = True

        response = {
            "ok" : status,
            "Content" : posts
        }
        return Response(response)

    def create(self,request):
        binary_payload = request.data
        # stream = io.BytesIO(binary_payload)
        # data = JSONParser().parse(stream)
        
        serializer = PostSaveSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(request.data)
        else:
            return Response({"errors": serializers.errors})