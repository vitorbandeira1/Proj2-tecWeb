from django.shortcuts import render
from .models import TextField
import requests,json,csv,os


API_key = '84a233083aa87fc033b3c55446e4dd3e'
Movie_ID = '464052'

def index(request):
    imdb = get_data(API_key,Movie_ID)
    print(imdb)
    return render(request, 'moviegenerator/teste.html')

#document all the parameters as variables
#write a function to compose the query using the parameters provided
def get_data(API_key, Movie_ID):
    query = 'https://api.themoviedb.org/3/movie/'+Movie_ID+'?api_key='+API_key+'&language=en-US'
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