from django.shortcuts import render, redirect
from .models import Post

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    if request.method == "POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        Post.objects.create(title=title, content=content)
    return redirect('posts:main')    

def main(request):
    posts = Post.objects.all()
    return render(request, 'posts/main.html', {'posts': posts})   

def main2(request):
    posts = Post.objects.all()
    return render(request, 'posts/main2.html', {'posts': posts})   
    
def main3(request):
    posts = Post.objects.all()
    return render(request, 'posts/main3.html', {'posts': posts})   
    
def main4(request):
    posts = Post.objects.all()
    return render(request, 'posts/main4.html', {'posts': posts})   

def main5(request):
    posts = Post.objects.all()
    return render(request, 'posts/main5.html', {'posts': posts})   


def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'posts/show.html', {'posts': post})
