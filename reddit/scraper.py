from selenium import webdriver
import urllib.request

driver = webdriver.Firefox()
#desired_url = input('What subreddit do you want to scrape the images of?\n')
desired_url = 'earthporn'
driver.get('http://imgur.com/r/'+desired_url)

# All images are in a div with id "imagelist"
# Each image in a div with class "post"
# Each "post" div has a <a> tag with a href
# GET THAT HREF
# download it

imagelist = driver.find_element_by_id('imagelist') # Div of images
posts = imagelist.find_elements_by_class_name('post') # Each post

for post in posts:


driver.close()