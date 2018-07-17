# hello.py
"""Hello world, Python"""

import MoviesNester

print("---练习1---")
print("Hello, Python!")
print("------")

print("---练习2---")
Movies = ["The Holy Grail", "The Life of Brain", "The Meaning of Life"]
print(Movies[2])
print(Movies[1])
print(Movies[0])
print("---")
print(Movies)
print("---")
CAST = ["Cheese", "Plain", "Jones", "Idell"]
print("cast: ", CAST)
print("cast Len: ", len(CAST))
print("cast[1]: ", CAST[1])

print("---练习3---")
CAST.append("Gilliam")
print("cast append:Gilliam>", CAST)
CAST.pop()
print("cast pop:Gilliam>print", CAST)

CAST.extend(["Gilliam", "Chapman"])
print("cast extend:['Gilliam', 'Chapman']>", CAST)
CAST.pop()
print(CAST)
CAST.pop()
print(CAST)
CAST.pop()
print(CAST)
CAST.remove("Plain")
print(CAST)
CAST.insert(0, "PlainNew")
print(CAST)

print("---MoviesNester.print_lol(Movies)---")
MoviesNester.print_lol(CAST, 1)
