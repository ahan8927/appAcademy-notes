# Lists
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# supplies = ['crayons', 'pencils', 'paper', 'Kleenex', 'eraser']
# print(supplies)

# supplies.append('markers')
# print(supplies)

# supplies.remove('crayons')
# print(supplies)

# supplies.sort()
# print(supplies)

# supplies.sort(key=str.lower)
# print(supplies)

# -------

# colors = ['red', 'blue', 'green', 'pink']
# # print(colors)

# alphabetical = sorted(colors, reverse=True)
# print(colors)
# print(alphabetical)

# reverseColors = reversed(colors)
# print(list(reverseColors))

# -------

# scores = [150, 210, 188, 76]
# print(scores)
# print(sum(scores))
# print(max(scores))
# print(min(scores))
# print(sum(scores) / len(scores))
# print(sorted(scores, reverse=True))

# TUPLES
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# b = ('a', 'b', 'c', 'd', 'e')
# c = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 # without parans
# print(a, b)

# shopping = ('apples', 'milk', 'bread')
# print(tuple(sorted(shopping)))

# ------

# shoppingStops = (  # Tuple of arrays
#     ['bread', 'milk', 'eggs'],
#     ['picture hooks'],
# )

# users = [ # list of tuples
#     (1, 'user1'),
#     (2, 'user2')
# ]
# print(shoppingStops)
# print(shoppingStops[0][0])

# ------

# scores = (15, 22, 66, 34, 99, 29, 54)
# print(scores)
# print(max(scores))
# print(sum(scores) / len(scores))
# print(tuple(sorted(scores)))


# def minmax(num):
#     return min(num), max(num)


# print(minmax(scores))
# (lowest, highest) = minmax(scores)  # multiple returns from functions
# print(highest, lowest)

# ------

# a = 1, 2, 3
# b = ('a', 'b', 'c')

# empty = ()
# print(empty)

# single = (1,)
# print(single)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# RANGES

# nums = range(10)
# print(list(nums))

# counting = range(1, 11)
# print(list(counting))

# fives = range(0, 51, 5)
# print(list(fives))

# items = ['a', 'b', 'c']
# for i in range(len(items)):
#     print(i, items[i])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Dictionaries

# book = {
#     'title': 'Goodnight Moon',
#     'rating': 7492,
#     'stars': 50.5,
#     'author': {
#         'firstName': 'Aaron',
#         'lastName': 'Hanson'
#     },
#     'images': ['goodnight.png', 'goodnight2.png'],
# }
# print(book)
# print(len(book))

# del book['stars']
# print(book)

# book['stars'] = 4.8
# print(book)

# for i in book:
#     print(i, book[i])

# ------------

# pond = dict(
#     depth=10,
#     area='210 square feet',
#     fish=['mary', 'bob', 'billy'],
# )

# print(pond)

# alligator = dict([
#     ('lifespan', 50),
#     ('length', 3.4),
#     ('apple', 1),
#     ('banana', 'yum'),
#     ('bee', 'yellow'),
# ])

# print(alligator)

# keys = ['name', 'home runs', 'strikeouts', 'rbi']
# values = ['Babe Ruth', 7214, 1330, 2214]
# player = dict(zip(keys, values))
# print(player)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# SETS

# a = set('banana')
# b = set('scarab')
# print(a, b)

# print(a | b)
# print(a.union(b))

# print(a & b)
# print(a.intersection(b))

# print(a ^ b)
# print(a.symmetric_difference(b))

# print(a - b)
# print(a.difference(b))

# error
# print(a + b) unsupported operand

# purchasingEmails = ('bob@gmail.com', 'sam@yahoo.com', 'riley@rileymail.org')
# helpEmails = ('jo@josbilling.com', 'bob@gmail.com', 'sam@yahoo.com')

# print('Users making a purchase and also calling help desk')
# print(set(purchasingEmails) & set(helpEmails))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PROCESSING LISTS

# all() - looking for any item that is false
# title1 = ['Mr', 'Mrs', 'Ms']
# title2 = ['Mr', 'Mrs', 'Ms', '']
# title3 = []
# title4 = ['', '', '', '']

# print(all(title1))
# print(all(title2))
# print(all(title3))
# print(all(title4))

# any() - looking for any item to be true
# feedback1 = ['', '', '', '']
# feedback2 = ['So much fun!', '', '', '']
# feedback3 = []

# print(any(feedback1), feedback1)
# print(any(feedback2), feedback2)
# print(any(feedback3), feedback3)

# ---------------

# MAP()
# scores = [90, 86, 45, 67, 78, 98, 23, 45, 87, 98]

# def isA(num):
#     return num >= 90

# # print(list(filter(isA, scores)))

# def getGrade(num):
#     if (num >= 90):
#         return 'A'
#     elif (num < 90 and num >= 80):
#         return 'B'
#     elif (num < 80 and num >= 70):
#         return 'C'
#     elif (num < 70 and num >= 60):
#         return 'D'
#     else:
#         return 'D'

# grades = list(map(getGrade, scores))
# # print(grades)
# # print('ZIPPED GRADES AND SCORES')

# print(list(zip(scores, grades)))

# test = ['a']
# print('yes' if len(test) == 1 else 'no')  # TERNARY
