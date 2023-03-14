from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie,Slides
from .forms import MovieForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
def movie_list(request):
    movie = Movie.objects.all()
    movie_paginator = Paginator(movie,5)
    page = movie_paginator.get_page(1)
    if request.method== "GET":
        st=request.GET.get('searchname')
        if st !=None:
            movie= Movie.objects.filter(name__icontains=st)
    return render(request,'movielist.html',{'count':movie_paginator.count,'pagee':page,'movie':movie})

def add_movie(request):
    form = Movie.objects.all()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request,'addmovie.html',{'form':form})


def update_movie(request, id):
    movie = Movie.object.get(id=id)
    form = MovieForm(instance=movie)
    if request == 'POST':
        form = MovieForm(request.Post,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/movie')
    return render(request,'updatemovie.html',{'form':form})

def movie_details(request,id):
    movie= get_object_or_404(Movie,pk=id)
    return render(request,'moviedetails.html',{'movie':movie})


def delete_movie(request,id):
    movie = Movie.objects.filter(id=id).delete()
    return redirect('/')

def SlidesPage(request):
    sld = Slides.objects.all()
    return render(request,'Slides.html',{'slid':Slides})

def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your Password does not Match")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('/')
    return render(request,'signup.html')