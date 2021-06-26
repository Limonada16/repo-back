from blog.serializer import PostSerializer
import io
from blog.models import Post
import json
from datetime import date, datetime
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import time
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.renderers import JSONRenderer


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        data = request.POST
        try:
            user = User.objects.get(username=data["user"])
            if user.check_password(data["password"]):
                return HttpResponse("OK")
            else:
                return render(request, "login.html", {"flag": True})
        except:
            return render(request, "login.html", {"flag": True})
        



@csrf_exempt
def createpost(request):
    json_data = "{\"content\": \"mi twtit\"}"
    #strean = io.StringIO(json_data)
    #item = JSONParser.parse(json_data)
    item = json.loads(json_data)
    print(item["content"])
    return HttpResponse("ok")

def serialize_demo(request):
    post = Post.objects.first()
    serializer = PostSerializer(post)
    return serializer.data
# Create your views here.
@cache_page(60)
def slow_api(request):
    time.sleep(4)
    return HttpResponse("done")

def whoiam(request):
    return HttpResponse(str(request.META['HTTP_HOST']))
def hello_world(request):

    posts = Post.objects.all()
    data = serializers.serialize("json", posts)
    print(data)
    
    items = serializers.serialize("json", data)
    for item in items:
        print(item.__dict__)
    return HttpResponse("ok")
