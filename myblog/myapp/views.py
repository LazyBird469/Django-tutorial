from django.shortcuts import render, redirect, HttpResponse
from .models import Post,Myfriend,Blog
from .forms import *

# Create your views here.
def postdata(request):
    post_data = Post.objects.all()
    context = {'data': post_data}
    return render(request, 'posts.html', context)

def myfriends_view(request):
    print("Myfriends view called")
    friends = Myfriend.objects.all()
    mylist = [1,2,3,4,5]
    context = {'friends': friends, 'mylist': mylist}
    return render(request, 'myfriends.html', context)

def postdetail(request, pk):
    data = Post.objects.filter(id=pk)
    getdata = Post.objects.get(id=pk) # single query
    context = {"data": data, "getdata": getdata}
    return render(request, 'detail.html', context)

def createpost(request):
 
 if request.method == 'POST':
    title = request.POST.get('title')
    body = request.POST.get('post_body')
    photo = request.FILES.get('photo')
    print(title, body, photo)
    query = Post.objects.create(title=title, post_body=body, image=photo)
    print('Successfully created post')
    return redirect("/posts/")
 return render(request, 'createpost.html')

def createform(request):
   fm = PostModelForm()
   if request.method == 'POST':
      fm = PostModelForm(request.POST, request.FILES)
      if fm.is_valid():
            print(fm)
            fm.save()
            print('Successfully created post')
            return redirect('/posts/')
      else:
            print('Error in form')
            return HttpResponse('Error')
   return render(request, 'createpost.html', {'fm': fm})

def deleteblog(request, pk):
    getdata = Blog.objects.get(id=pk)
    getdata.delete()
    return redirect('/bloglist/')

def createblog(request):
    bg = BlogModelForm()
    if request.method == 'POST':
        bg = BlogModelForm(request.POST, request.FILES)
        if bg.is_valid():
            print(bg)
            bg.save()
            print('Successfully created blog')
            return redirect('/bloglist/')
        else:
            print('Error in form')
            return HttpResponse('Error')
    return render(request, 'createblog.html', {'bg': bg})

def bloglist(request):
    blogs = Blog.objects.all()
    return render(request, 'bloglist.html', {'blogs': blogs,})


def blogupdate(request, pk):
    blog_obj = Blog.objects.filter(id=pk)                 #update
    get_title = request.POST.get('title')
    get_body = request.POST.get('body')
    img = request.FILES.get('image')
    blog_obj.update(title=get_title, post_body=get_body, image=img)
    return redirect('/bloglist/')
    
# def blogupdate(request, pk):
#     blog_obj = Blog.objects.get(id=pk)
#     if request.method == 'POST':
#         blog_obj.title = request.POST.get('title')
#         blog_obj.post_body = request.POST.get('body')
#         img = request.FILES.get('image')
#         if img:
#             blog_obj.image = img
#         blog_obj.save()
#         return redirect('/bloglist/')
#     return render(request, 'blogupdate.html', {'blog': blog_obj})

# def blogupdate(request, pk):
#     if request.method == 'POST':
#         get_title = request.POST.get('title')
#         get_body = request.POST.get('body')
#         img = request.FILES.get('image')
#         update_data = {'title': get_title, 'post_body': get_body}
#         if img:
#             update_data['image'] = img
#         Blog.objects.filter(id=pk).update(**update_data)
#     return redirect('/bloglist/')