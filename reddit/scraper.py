# TODO:
# Create a directory named desired_url
# Save images in that

from selenium import webdriver
import urllib.request 
import os

driver = webdriver.Firefox()
#desired_url = input('What subreddit do you want to scrape the images of?\n')
desired_url = 'earthporn'
driver.get('http://imgur.com/r/'+desired_url)

imagelist = driver.find_element_by_id('imagelist') # Div of images
links = imagelist.find_elements_by_tag_name('a') # Each link of post

# I couldn't make this into a list comprehension because
# Apparently, links isn't an iterable
hrefs = []
for link in links:
	href = link.get_attribute("href")
	if desired_url in href:
		hrefs.append(href)

for (i, source) in enumerate(hrefs):
	driver.get(source)
	img_div = driver.find_element_by_class_name('post-image')
	src = img_div.find_element_by_tag_name('img').get_attribute('src')
	urllib.request.urlretrieve(src, str(i)+".jpg") # The line that saves


driver.close()