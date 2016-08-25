from selenium import webdriver
import urllib.request 
import os

driver = webdriver.Firefox()
desired_url = input('What subreddit do you want to scrape the images of?\n')
driver.get('http://imgur.com/r/'+desired_url)

# This whole thing is folder behavior.
# Let's say you type in 'earthporn'. It creates a file named 'earthporn1'
# But what if you aleady have 'earthporn1'? If you do, it creates 'earthporn2'
# And so on.
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

# Collecting hrefs. 
hrefs = [link.get_attribute('href') for link in links if desired_url in link.get_attribute('href')]
# hrefs = [href for href in link.get_attribute("href") if desired_url in href for link in links] didn't work
# For every for loop involving lists, there is a list comprehension for it.
#hrefs = []
#for link in links:
#	href = link.get_attribute("href")
#	if desired_url in href:
#		hrefs.append(href)

# Going to the href of where each image is and saving it.
for (i, source) in enumerate(hrefs):
	driver.get(source)
	img_div = driver.find_element_by_class_name('post-image')
	src = img_div.find_element_by_tag_name('img').get_attribute('src')
	fullfilename = os.path.join(desired_folder, str(i)+".jpg") # what folder i want to save it in, what i want to save it as
	urllib.request.urlretrieve(src, fullfilename) # The line that saves it
	print('Saving ' + src + '....')

driver.close()