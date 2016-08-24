# Scraping a certain movie/TV show.

from selenium import webdriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable

def display(title, rating, description, cast):
	return "\n\nTitle: {}\nRating: {}\nDescription: {}\nStarring:\n {}\n".format(title, rating, description, cast)

def find_content(film):
	# Navigating
	search_bar.send_keys(film)
	search_click.click()
	selection_div = driver.find_element_by_class_name("findSection") # Div where the results are
	selection_links = [link for link in selection_div.find_elements_by_tag_name("a") if link.text] # All results
	selection_links[0].click() # Click first result

	# Collecting data
	content_title = driver.find_element_by_tag_name('h1').text
	content_rating_div = driver.find_element_by_class_name('ratingValue')
	content_rating = content_rating_div.find_element_by_tag_name('span').text
	content_description = driver.find_element_by_class_name('summary_text').text
	content_cast_table = driver.find_element_by_class_name('cast_list')
	content_cast_list = content_cast_table.find_elements_by_tag_name('span')
	content_cast = [c.text for c in content_cast_list][:8]
	content_display = display(content_title, content_rating, content_description, content_cast)
	return content_display

film = input("What'chu wanna know about?\n")

driver = webdriver.Firefox()
driver.get('http://www.imdb.com/')
search_bar = driver.find_element_by_id("navbar-query")
search_click = driver.find_element_by_id("navbar-submit-button")

print(find_content(film))
driver.close()