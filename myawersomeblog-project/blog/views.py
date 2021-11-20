from django.shortcuts import render


# Create your views here.
def showblog(request):
    return render(request, 'blog/blog.html')
