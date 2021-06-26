"""microblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import hello_world, createpost, serialize_demo, login, slow_api, whoiam
from blog.viewsets import PostViewset, tokenizer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login),
    path('hello', hello_world),
    path('slow_api', slow_api),
    path('posts', PostViewset.as_view({'get':'list', 'post': 'create'})),
    path('post/<id>', PostViewset.as_view({'get': 'retrieve'})),
    path('tokenaize', tokenizer.as_view({'post': 'get_token'})),
    path('whoiam', whoiam)
    
]

