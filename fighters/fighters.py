from selenium import webdriver
from collections import namedtuple
import urllib.request

Record = namedtuple('Record', ['N', 'W', 'L', 'D'])

def extract_record_string(article):
	full_record = article.find_element_by_tag_name("h2").text.split('\n')[0].split(' ')[0] # 12-1-0
	separate_record = full_record.split('-')
	return separate_record # ('12', '1', '0')

driver = webdriver.Firefox()
START_URL = "http://m.ufc.ca/fighter/"
fighter_one = "Ronda Rousey".replace(' ', '-') #input("Enter a fighter's full name.")
fighter_two = "Chad Mendes".replace(' ', '-') #input("Enter another fighter's full name.")

def get_record(fighter):
	driver.get(START_URL+fighter)
	article = driver.find_element_by_class_name("fighter-profile")
	record = extract_record_string(article)
	record_tuple = Record(N=fighter, W=record[0], L=record[1], D=record[2])
	return record_tuple

f1 = get_record(fighter_one)
f2 = get_record(fighter_two)
driver.close()