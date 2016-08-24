from prettytable import PrettyTable
import scraper

table = PrettyTable(['Latest Movies', 'Top Shows'])
movies = scraper.collect_movies()
tvshows = scraper.collect_tv_shows()

def display_collections(collection):
	for item in collection:
		table.add_row([item])

display_collection(movies)
display_collection(tvshows)
print(table)