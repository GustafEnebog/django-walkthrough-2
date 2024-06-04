from django.shortcuts import render, get_object_or_404
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

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )
