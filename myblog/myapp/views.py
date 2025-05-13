from django.shortcuts import render
from .models import Post,Myfriend

# Create your views here.
    post_data = Post.objects.all()
    context = {'data': post_data}
    return render(request, 'posts.html', context)

def myfriends_view(request):
    print("Myfriends view called")
    friends = Myfriend.objects.all()
    mylist = [1,2,3,4,5]
    context = {'friends': friends, 'mylist': mylist}
    return render(request, 'myfriends.html', context)