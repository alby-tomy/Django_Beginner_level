from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieApp import movieUpdation
from . models import Movie


# Create your views here.
def indexName(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html',context)

def detailsView(request, movieId):

    movie_id = Movie.objects.get(id=movieId)
    return render(request, 'detail.html',{'movie_id':movie_id})

def updateView(request, movieId):
    movieID = Movie.objects.get(id=movieId)
    formUpdate = movieUpdation.MovieUpdate(request.POST or None, request.FILES, instance=movieID)
    if formUpdate.is_valid():
       formUpdate.save()
       return redirect('/')
    return render(request, 'update.html',{'formU':formUpdate,'movie-id':movieID})

def addItemsView(request):
    if request.method == 'POST':
        add_name = request.POST.get('name')
        add_descri = request.POST.get('description')
        add_year = request.POST.get('year')
        add_image = request.FILES['image']

        addMovie = Movie(name=add_name, description=add_descri, year=add_year, image=add_image)
        addMovie.save()
    return render(request, 'addItem.html')

def deleteView(request, movieId):
    if request.method == 'POST':
        movie_id = Movie.objects.get(id=movieId)
        movie_id.delete()
        return redirect('/')
    return render(request,'delete.html')
