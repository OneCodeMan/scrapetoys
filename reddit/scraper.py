# TODO:
# Look for folders
# Store in list
# Folder name: folder_names[-1] + 1

from selenium import webdriver
import urllib.request 
import os

driver = webdriver.Firefox()
#desired_url = input('What subreddit do you want to scrape the images of?\n')
desired_url = 'earthporn'
driver.get('http://imgur.com/r/'+desired_url)

folder_exists = False
folder_version = 1

while not folder_exists:
	desired_folder = desired_url[:] + str(folder_version)

	if os.path.exists(desired_folder):
		folder_version += 1
	else:
		os.makedirs(desired_folder)
		folder_exists = True

imagelist = driver.find_element_by_id('imagelist') # Div of images
links = imagelist.find_elements_by_tag_name('a') # Each link of post

hrefs = []
for link in links:
	href = link.get_attribute("href")
	if desired_url in href:
		hrefs.append(href)

for (i, source) in enumerate(hrefs):
	driver.get(source)
	img_div = driver.find_element_by_class_name('post-image')
	src = img_div.find_element_by_tag_name('img').get_attribute('src')
	fullfilename = os.path.join(desired_folder, str(i)+".jpg")
	urllib.request.urlretrieve(src, fullfilename) # The line that saves
	print('Saving ' + src + '....')


driver.close()