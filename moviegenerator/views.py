from django.shortcuts import render
from .models import Production
import requests,json,csv,os,random



api_key = '84a233083aa87fc033b3c55446e4dd3e'
movie_id = '464052'
tv_id = '1416'
access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NGEyMzMwODNhYTg3ZmMwMzNiM2M1NTQ0NmU0ZGQzZSIsInN1YiI6IjYwOGIxNzk3NjY0NjlhMDAyYjFiMzM1OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dmwOZBSInOqzZLh8CdeUHPqH-jq47ZQwAfYsd86AxpY'

rating = 8.0
genre = 28

def index(request):
    #imdb = get_data(API_key,Movie_ID)
    #getMovie(movie_id)
    #getTv(tv_id)
    results = randomizer(discoverMovie(rating, genre))
    details = getDetails(results)
    x = getMovieWatchProviders(details["id"])
    #getGeneroMovie()
    genresTv = getGeneroTv()['genres']
    genresdict = {}
    for i in genresTv:
        values = list(i.values())
        genresdict[values[0]] = values[1]
        print(genresdict)
        
        # genero =i.values()
        # for j in i.values():
        #     print(j)
    details["dictTV"]=genresdict
    print(details)

    return render(request, 'moviegenerator/teste.html', details)

def mylist(request):
    return render(request, 'moviegenerator/mylist.html')
    


# Defs pra explorar api ########################################

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


def getMovieWatchProviders(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={api_key}"
    response = requests.get(url)
    if response.status_code==200: 
        movieData = json.loads(response.text) #response dictionary
        return movieData["results"]["BR"] #providers from brazil
    else:
        return ("error")

def getTvWatchProviders(tv_id):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}/watch/providers?api_key={api_key}"
    response = requests.get(url)
    if response.status_code==200: 
        tvData = json.loads(response.text) #response dictionary
        return tvData["results"]["BR"] #providers from brazil
    else:
        return ("error")

def discoverMovie(rating, genre):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=2&vote_average.gte={rating}&with_genres={genre}&with_watch_monetization_types=flatrate"
    response = requests.get(url)
    if response.status_code==200: 
        movieData = json.loads(response.text) #response dictionary
        #print(movieData["results"])
        return movieData["results"] #providers from brazil
    else:
        return ("error")

def discoverTv(rating, genre):
    url = f"https://api.themoviedb.org/3/discover/tv?api_key={api_key}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=2&vote_average.gte={rating}&with_genres={genre}&with_watch_monetization_types=flatrate"
    response = requests.get(url)
    if response.status_code==200: 
        movieData = json.loads(response.text) #response dictionary
        #print(movieData["results"])
        return movieData["results"] #providers from brazil
    else:
        return ("error")

def randomizer(lista):
    return random.choice(lista)

def getDetails(results):
    img = results["poster_path"]
    title = results["original_title"] 
    overview = results["overview"]
    id = results["id"]
    link = getMovieWatchProviders(id)["link"]
    details =  {"img": f"https://image.tmdb.org/t/p/w500/{img}",
                "title": title,
                "id": id,
                "overview": overview,
                "link": link}
    return details
    
def getGeneroMovie():
    url = 'https://api.themoviedb.org/3/genre/movie/list?api_key='+api_key+'&language=en-US'
    #urlTv = 'https://api.themoviedb.org/3/genre/tv/list?api_key='+API_key+'&language=en-US'
    response =  requests.get(url)
    #responseTv =  requests.get(urlTv)
    if response.status_code==200: 
        genresMovie = json.loads(response.text)
        print(genresMovie)
        return (genresMovie)
    else:
        return ("error")

def getGeneroTv():
    urlTv = 'https://api.themoviedb.org/3/genre/tv/list?api_key='+api_key+'&language=en-US'
    response =  requests.get(urlTv)
    if response.status_code==200: 
        genresTv = json.loads(response.text)
        
        return (genresTv)
    else:
        return ("error")



    

        
