from django.shortcuts import render
from .models import TextField
import requests,json,csv,os



api_key = '84a233083aa87fc033b3c55446e4dd3e'
movie_id = '464052'
tv_id = '1416'
access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NGEyMzMwODNhYTg3ZmMwMzNiM2M1NTQ0NmU0ZGQzZSIsInN1YiI6IjYwOGIxNzk3NjY0NjlhMDAyYjFiMzM1OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dmwOZBSInOqzZLh8CdeUHPqH-jq47ZQwAfYsd86AxpY'

def index(request):
    #imdb = get_data(API_key,Movie_ID)
    getMovie(movie_id)
    getTv(tv_id)
    getWatchProviders(tv_id)
    return render(request, 'moviegenerator/teste.html')


def getMovie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    if response.status_code==200: 
        movieData = json.loads(response.text) #response dictionary
        return movieData
    else:
        return ("error")

def getTv(tv_id):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)


def getWatchProviders(tv_id):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}/watch/providers?api_key={api_key}"
    response = requests.get(url)
    if response.status_code==200: 
        tvData = json.loads(response.text) #response dictionary
        return tvData["results"]["BR"] #providers from brazil
    else:
        return ("error")

        
