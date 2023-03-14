from django.urls import path
from .views import *


urlpatterns = [
    path('',SlidesPage),
    path('movielist',movie_list),
    path('add movie',add_movie),
    path('movie-details/<int:id>',movie_details),
    path('update-movie/<int:id>',update_movie),
    path('delet-movie/<int:id>',delete_movie),
    path('signup',Signup)

]