from django.shortcuts import render
from .models import Production
from django.conf import settings
import requests,json,csv,os,random



api_key = settings.TMDB_API_KEY
access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NGEyMzMwODNhYTg3ZmMwMzNiM2M1NTQ0NmU0ZGQzZSIsInN1YiI6IjYwOGIxNzk3NjY0NjlhMDAyYjFiMzM1OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dmwOZBSInOqzZLh8CdeUHPqH-jq47ZQwAfYsd86AxpY'

def index(request):
	details = {}
	title = ''
	if request.method == 'POST':
		#genres = int(request.POST.get('genres'))
		#rating = float(request.POST.get('rating'))
		#type_of = request.POST.get('type')

		

		# print(genres, rating, type_of)

		if 'taskAdd' in request.POST:
			print('entrou if taskadd')
			# title = Production().save()
		else:
			genres = request.POST.get('genres')
			print(genres)
			for k, v in genres.items():
				print(v)
			rating = float(request.POST.get('rating'))
			type_of = request.POST.get('type')
			print('entrou else taskadd')
			#chama as funcoes pra pegar o filme aleatorio
			if type_of == "movie": 
				title = randomizer(discoverMovie(rating, genre))
			
			elif type_of == "tv":
				title = randomizer(discoverTv(rating, genre))

			production = getProduction(type_of, title["id"])
			details = getDetails(type_of, production)
			print(details)
	genresMovie, genresTv = getGenero()
	# print('Movie',genresMovie,'\nTv',genresTv)
	details["genresMovie"] = genresMovie
	details["genresTv"] = genresTv


	return render(request, 'moviegenerator/teste.html', details)

def mylist(request):
	return render(request, 'moviegenerator/mylist.html')
	


# Defs pra explorar api ########################################

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

		# if tvData["results"] == "BR":
		# 	print('PROVIDER == DE BR' ,tvData["results"])
		# 	# return movieData["results"]["BR"] #providers from brazil
		# else:
		# 	print('PROVIDER DIFF DE BR' ,tvData["results"])
		# 	# return movieData["results"]["US"] #providers from brazil

		return tvData["results"]["BR"] #providers from brazil
	else:
		return ("error")


def discoverMovie(rating, genre):
	url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=2&vote_average.gte={rating}&with_genres={genre}&with_watch_monetization_types=flatrate"
	response = requests.get(url)
	if response.status_code==200: 
		movieData = json.loads(response.text) #response dictionary
		return movieData["results"] #providers from brazil
	else:
		return ("error")

def discoverTv(rating, genre):
	url = f"https://api.themoviedb.org/3/discover/tv?api_key={api_key}&language=en-US&sort_by=popularity.desc&page=1&vote_average.gte={rating}&without_genres={genre}&include_null_first_air_dates=false&with_watch_monetization_types=flatrate"
	response = requests.get(url)
	if response.status_code==200: 
		tvData = json.loads(response.text) #response dictionary
		return tvData["results"] #providers from brazil
	else:
		return ("error")

def randomizer(lista):
	return random.choice(lista)

def getProduction(type, tv_id):
	url = f"https://api.themoviedb.org/3/{type}/{tv_id}?api_key={api_key}&language=en-US"
	response = requests.get(url)
	if response.status_code==200: 
		movieData = json.loads(response.text) #response dictionary
		return movieData #providers from brazil
	else:
		return ("error")

def getDetails(type_of, results):
	img = results["poster_path"]
	if type_of == "movie":
		title = results["original_title"]
		year = (results["release_date"]).split("-")[0]
	elif type_of == "tv":
		title = results["original_name"]
		year = (results["first_air_date"]).split("-")[0]
	overview = results["overview"]
	id = results["id"]
	popularity = results["popularity"]
	rating = results["vote_average"]
	link = getWatchProviders(type_of, id)["link"]
	details =  {"img": f"https://image.tmdb.org/t/p/w500/{img}",
				"title": title,
				"id": id,
				"overview": overview,
				"link": link,
				"popularity": popularity,
				"rating": rating,
				"year": year}
	return details

def getWatchProviders(type, id):
	url = f"https://api.themoviedb.org/3/{type}/{id}/watch/providers?api_key={api_key}"
	response = requests.get(url)
	if response.status_code==200: 
		data = json.loads(response.text) #response dictionary
		return data["results"]["BR"] #providers from brazil
	else:
		return ("error")

def getGeneroMovie():
	url = 'https://api.themoviedb.org/3/genre/movie/list?api_key='+api_key+'&language=en-US'
	#urlTv = 'https://api.themoviedb.org/3/genre/tv/list?api_key='+API_key+'&language=en-US'
	response =  requests.get(url)
	#responseTv =  requests.get(urlTv)
	if response.status_code==200: 
		genresMovie = json.loads(response.text)
		# print(genresMovie)
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

def getGenero():
	genresTv = getGeneroTv()['genres']
	genresMovie = getGeneroMovie()['genres']
	#genres = genresTv+genresMovie
	genresMovieDict = {}
	genresTvDict = {}

	for i in genresTv:
		values = list(i.values())
		genresTvDict[values[0]] = values[1]
	for j in genresMovie:
		values = list(j.values())
		genresMovieDict[values[0]] = values[1]
	
	return genresMovieDict,genresTvDict
