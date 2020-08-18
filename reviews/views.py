from django.shortcuts import render, redirect, get_object_or_404
from .models import Review

def new(request):
    return render(request, 'reviews/new.html')

def new2(request):
    return render(request, 'reviews/new2.html')


def create(request):
    if request.method == "POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        image=request.FILES.get('image')
        user = request.user
        Review.objects.create(title=title, content=content, image=image, user=user)
        return redirect('reviews:main')  

def main(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/main.html', {'reviews':reviews})

def show(request, id):
    review = Review.objects.get(pk=id)
    return render(request, 'reviews/show.html', {'review': review})

def update(request, id):
    review=get_object_or_404(Review, pk=id)
    if request.method=="POST":
        review.title=request.POST['title']    
        review.content=request.POST['content']
        review.image=request.FILES.get('image')
        review.save()
        return redirect('reviews:show',review.id)
    return render(request, 'reviews/update.html', {"review":review})

def delete(request, id):
    review = get_object_or_404(Review, pk=id)
    review.delete()
    return redirect('reviews:main')    