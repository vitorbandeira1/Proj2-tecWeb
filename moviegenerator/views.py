from django.shortcuts import render
from .models import TextField
import requests,json,csv,os


API_key = '84a233083aa87fc033b3c55446e4dd3e'
Movie_ID = '464052'
Tv_ID = ''

def index(request):
    # imdb = get_data(API_key,Movie_ID)
    generos = get_genero(API_key)
    print(generos)
    return render(request, 'moviegenerator/teste.html')

#document all the parameters as variables
#write a function to compose the query using the parameters provided
def get_details(API_key, Movie_ID):
    queryMovie = 'https://api.themoviedb.org/3/movie/'+Movie_ID+'?api_key='+API_key+'&language=en-US'
    queryShow = 'https://api.themoviedb.org/3/tv/'+Tv_ID+'?api_key='+API_key+'&language=en-US'
    response =  requests.get(query)
    print(response)
    if response.status_code==200: 
    #status code ==200 indicates the API query was successful
        array = response.json()
        text = json.dumps(array)
        print(text)
        return (text)
    else:
        return ("error")

def get_genero(API_key):
    queryMovie = 'https://api.themoviedb.org/3/genre/movie/list?api_key='+API_key+'&language=en-US'
    queryShow = 'https://api.themoviedb.org/3/genre/tv/list?api_key='+API_key+'&language=en-US'
    response =  requests.get(queryShow)
    print(response)
    if response.status_code==200: 
    #status code ==200 indicates the API query was successful
        array = response.json()
        text = json.dumps(array)
        print(text)
        return (text)
    else:
        return ("error")

def get_review(API_key, Movie_ID):
    queryMovie = 'https://api.themoviedb.org/3/movie/'+Movie_ID+'/reviews?api_key='+API_key+'&language=en-US&page=1'
    queryShow = 'https://api.themoviedb.org/3/tv/'+Tv_ID+'/reviews?api_key='+API_key+'&language=en-US&page=1'
    response =  requests.get(queryShow)
    print(response)
    if response.status_code==200: 
    #status code ==200 indicates the API query was successful
        array = response.json()
        text = json.dumps(array)
        print(text)
        return (text)
    else:
        return ("error")