from django.shortcuts import render, redirect
from .models import Production
from django.conf import settings
import requests,json,csv,os,random



api_key = settings.TMDB_API_KEY
access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NGEyMzMwODNhYTg3ZmMwMzNiM2M1NTQ0NmU0ZGQzZSIsInN1YiI6IjYwOGIxNzk3NjY0NjlhMDAyYjFiMzM1OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dmwOZBSInOqzZLh8CdeUHPqH-jq47ZQwAfYsd86AxpY'

sort_list_movie=["popularity.asc", "popularity.desc", "release_date.desc", "revenue.asc", "revenue.desc", "primary_release_date.asc", "primary_release_date.desc", "original_title.asc", "original_title.desc", "vote_average.asc", "vote_average.desc",'vote_count.asc', 'vote_count.desc']

sort_list_tv=['vote_average.desc', 'vote_average.asc', 'first_air_date.desc', 'popularity.desc', 'popularity.asc']

def index(request):
	details = {}
	title = ''
	if request.method == 'POST':
		if 'taskAdd' in request.POST:
			title = request.POST.get('title')
			id_api = request.POST.get('id_api')
			rating = float(request.POST.get('rating'))
			link = request.POST.get('link')
			img = request.POST.get('img')
			type_of = request.POST.get('type_of')
			'''
			if not Production.objects.filter(type_of=type_of).exists():
				production = Production(id_api=id_api, title=title, rating=rating, link=link, img=img, type_of=type_of )
				production.save()
			'''
			production = Production(id_api=id_api, title=title, rating=rating, link=link, img=img, type_of=type_of )
			production.save()
			return render(request,"moviegenerator/teste.html")

		else:
			genres = request.POST.getlist('genres')
			genres = ','.join(genres) #de lista para string
			rating = float(request.POST.get('rating'))
			type_of = request.POST.get('type')
			print('entrou else taskadd')
			#chama as funcoes pra pegar o filme aleatorio
			if type_of == "movie": 
				title = randomizer(discoverMovie(rating, genres))
			
			elif type_of == "tv":
				title = randomizer(discoverTv(rating, genres))

			print(type(title))
			id_api = title["id"]
			production = getProduction(type_of, title["id"])
			details = getDetails(type_of, production)
			details["id_api"] = id_api
			details["type_of"] = type_of
			

	genresMovie, genresTv = getGenero()
	# print('Movie',genresMovie,'\nTv',genresTv)
	details["genresMovie"] = genresMovie
	details["genresTv"] = genresTv



	return render(request, 'moviegenerator/teste.html', details)

def mylist(request):
	all_productions = Production.objects.all()
	return render(request, 'moviegenerator/mylist.html', {"productions":all_productions})
	


# Defs pra explorar api ########################################

def discoverMovie(rating, genre):
	sort_by = randomizer(sort_list_movie)
	url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&sort_by={sort_by}&include_adult=false&include_video=false&page=2&vote_average.gte={rating}&with_genres={genre}&with_watch_monetization_types=flatrate"
	response = requests.get(url)
	if response.status_code==200: 
		movieData = json.loads(response.text) #response dictionary
		print(movieData["results"])
		return movieData["results"] #providers from brazil
	else:
		return ("error")

def discoverTv(rating, genre):
	sort_by = randomizer(sort_list_tv)
	url = f"https://api.themoviedb.org/3/discover/tv?api_key={api_key}&language=en-US&sort_by={sort_by}&page=1&vote_average.gte={rating}&without_genres={genre}&include_null_first_air_dates=false&with_watch_monetization_types=flatrate"
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
	if img:
		img = f"https://image.tmdb.org/t/p/w500/{img}"
	else:
		img=''
	if type_of == "movie":
		title = results["original_title"]
		if isinstance(results["release_date"], str) :
			year = (results["release_date"]).split("-")[0]
		else:
			year = ''
	elif type_of == "tv":
		title = results["original_name"]
		if isinstance(results["first_air_date"], str) :
			year = (results["first_air_date"]).split("-")[0]
		else:
			year = ''
	overview = results["overview"]
	id = results["id"]
	popularity = results["popularity"]
	rating = results["vote_average"]
	
	link = f'https://www.themoviedb.org/{type_of}/{id}' #getWatchProviders(type_of, id)["link"]
	details =  {"img": img,
				"title": title,
				"id": id,
				"overview": overview,
				"link": link,
				"popularity": popularity,
				"rating": rating,
				"year": year}
	return details

# def getWatchProviders(type, id):
# 	url = f"https://api.themoviedb.org/3/{type}/{id}/watch/providers?api_key={api_key}"
# 	response = requests.get(url)
# 	if response.status_code==200: 
# 		data = json.loads(response.text) #response dictionary
# 		return data["results"]["BR"] #providers from brazil
# 	else:
# 		return ("error")

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
