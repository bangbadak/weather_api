from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'community/community.html',
        {
            'posts': posts,
        },

    )

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'community/community_post.html',
        {
            'post': post,
        },
    )