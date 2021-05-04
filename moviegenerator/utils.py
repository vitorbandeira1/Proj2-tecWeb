import requests
from django.conf import settings

class TMDB(object):

    def __init__(self):

        if settings.TMDB_API_KEY is '':
            raise Exception('No TMDB_API_KEY given')

        self.api_key = settings.TMDB_API_KEY

    #def discoverMovie()

    def getMovie(self, movieID):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        if response.status_code==200: 
            movieData = json.loads(response.text) #response dictionary
            return movieData
        else:
            return ("error")
    
    def getTv(self, tvID):
        url = f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        if response.status_code==200: 
            tvData = json.loads(response.text) #response dictionary
            return tvData
        else:
            return ("error")

    
