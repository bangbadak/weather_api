from django.shortcuts import render
from .models import My_info
from community.models import Post
# Create your views here.
def index(request):
    my_info = My_info.objects.all()

    return render(
        request,
        'my_info/my_info.html',
        {
            'my_info': my_info
        }
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



