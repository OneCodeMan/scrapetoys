from selenium import webdriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable

driver = webdriver.Firefox()

def collect_movies():
	movie_link = driver.find_element_by_link_text('Movies')
	movie_titles = driver.find_elements_by_tag_name('h4')
	movie_titles_text = [title.text for title in movie_titles]
	driver.close()
	return movie_titles_text

def collect_tv_shows():
	driver.get("http://www.imdb.com/chart/toptv/")
	shows_div = driver.find_element_by_class_name("lister")
	show_titles = shows_div.find_elements_by_tag_name('a')
	show_titles_text = [show.text for show in show_titles if show.text]
	driver.close()
	return show_titles_text[:30]

table = PrettyTable(['Latest Movies', 'Top Shows'])