# movies.py
"""电影列表练习"""
from MoviesNester import print_lol

"""
movies=["The Holy Grail", 1975, "The Life of Brain", 1979,
	"Then Meaning of Life", 1983]
print(movies)

print("---for---")
for each_movie in movies:
	print(each_movie)

print("---while---")

count =0
while  count < len(movies):
	print(movies[count])
	count=count+1
"""

print("---列表套列表---")

MOVIES = \
	["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
		["Graham Chapman",
			["Michael Patin", "John Cheese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print(MOVIES)
print('\n')

"""
print("---def---")
def print_lol(the_list):
	for _list in the_list:
		if isinstance(_list, list):
			print_lol(_list)
		else:
			print(_list)
"""

print_lol(MOVIES, True, True, 0, 0, "movies.txt")
"""
try:
	with open("movies.txt", "w") as movies_file:
		print_lol(MOVIES, True, True, 0, 0, "movies.txt")
except IOError as run_error:
	print("Error: " + str(run_error))
"""
