from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5]  #this limits the number of blog posts to two
    return render(request,'blog/all_blogs.html',{'blogs':blogs})


def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)    #the blog_id comes from url.py, and from the address bar. 
    return render(request, 'blog/detail.html',{'blog':blog})


