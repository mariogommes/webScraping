import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent' : ua.chrome}
seeds = ["http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1"]

def get_description(link):
	for siblings in link.parent.find_next_siblings():
		if siblings.string != None:
			description = siblings.string

	return description

def find_film_list(link):
	response = requests.get(link, headers=header)

	if response.status_code == 200:		
		soup = BeautifulSoup(response.content, 'lxml')
		film_list = []

		for link in soup.body.find_all('a'):
			try:
				if link.parent['itemprop'] == 'name':
					film_list.append({link['title'] : get_description(link) })
			except KeyError:
				pass
	else:
		print("Status é diferente de 200, status: " + str(response.status_code))
		film_list = False

	return film_list

film_list = find_film_list(seeds[0])

if film_list != False:
	for movie in film_list:
		for movieName, description in movie.items():
			print("Título: ", movieName.strip('\n') + '\n')
			print("Sinopse: ")
			print(description.strip('\n'), end='\n\n')

