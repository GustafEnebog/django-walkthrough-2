from django.shortcuts import render
from django.views import generic
from .models import Post
# # Deleted according to instructions:  from django.http import HttpResponse

# Create your views here.
class PostList(generic.ListView):
    # Remove model = Post We can remove the model = Post as it is made redundant by the queryset 
    queryset = Post.objects.filter(status=1)    # before this row looked like this: queryset = Post.objects.all() but now we put a filter on it so that it not publish drafts!
    # Replaced by instruction: template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6

# def my_blog(request):
# Deleted according to instructions:   return HttpResponse("Hello, Blog!")