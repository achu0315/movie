from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieform
from .models import film


# Create your views here.
def demo(request):
    obj = film.objects.all()
    context = {
        'dm': obj
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = film.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        des = request.POST.get('des')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = film(name=name, dec=des, year=year, img=img)
        movie.save()

    return render(request, 'add.html')


def update(request,id):
    movie = film.objects.get(id=id)
    form = movieform(request.POST or None, request.FILES, instance=movie)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=film.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
