# TO DO
# Wrap this in a while True
# Wrap it in functions..
# Display 
# Then make it work for both titles and artists
# Wam bam shabam

from selenium import webdriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable

film = input("What'chu wanna know about?\n")

driver = webdriver.Firefox()
driver.get('http://www.imdb.com/')
search_bar = driver.find_element_by_id("navbar-query")
search_click = driver.find_element_by_id("navbar-submit-button")

search_bar.send_keys(film)
search_click.click()
selection_div = driver.find_element_by_class_name("findSection") # Div where the results are
selection_links = [link for link in selection_div.find_elements_by_tag_name("a") if link.text] # All results
selection_links[0].click() # Click first result

driver.close()