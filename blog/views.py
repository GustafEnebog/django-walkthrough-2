from django.shortcuts import render
from django.views import generic
from .models import Post
# # Deleted according to instructions:  from django.http import HttpResponse

# Create your views here.
class PostList(generic.ListView):
    # Remove model = Post We can remove the model = Post as it is made redundant by the queryset 
    queryset = Post.objects.all()
    template_name = "post_list.html"

# def my_blog(request):
# Deleted according to instructions:   return HttpResponse("Hello, Blog!")