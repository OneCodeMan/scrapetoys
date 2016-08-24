from selenium import webdriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable

driver = webdriver.Firefox()
driver.get('http://www.imdb.com/')

def collect_movies():
	movie_link = driver.find_element_by_link_text('Movies')
	movie_link.click()
	movie_titles = driver.find_elements_by_tag_name('h4')
	movie_titles_text = [title.text for title in movie_titles]
	return movie_titles_text

def collect_tv_shows():
	shows_link = driver.find_element_by_link_text('TV')
	shows_link.click()
	shows_div = driver.find_element_by_class_name("lister")
	show_titles = shows_div.find_elements_by_tag_name('a')
	show_titles_text = [show.text for show in show_titles if show.text]
	return show_titles_text

table = PrettyTable(['Latest Movies', 'Top Shows'])

# Column lengths need to match each other, ugh.
# The following code doesn't work:
# pairs = [[movie, show] for movie in movies for show in shows]
# It maps a movie to every show so the movie gets displayed
# More than once.

movies = collect_movies()
shows = collect_tv_shows()[:len(movies)-1]

driver.close()

for i in range(len(movies)-1):
	table.add_row([movies[i], shows[i]])

print(table)