from fruit import *

# An example random fruit basket
# randomBasket = [
#     [Fruit("orange1", 1), Fruit("apple5", 5), Fruit("banana3", 3), Fruit("orange4", 4), Fruit("apple1", 1),
#      Fruit("banana7", 7), Fruit("apple6", 6), Fruit("banana9", 9), Fruit("orange8", 8), Fruit("banana2", 2)],
#
#     [Fruit("apple2", 2), Fruit("banana1", 1), Fruit("apple3", 3), Fruit("orange2", 2), Fruit("banana4", 4),
#      Fruit("apple8", 8), Fruit("orange7", 7), Fruit("banana5", 5), Fruit("orange6", 6), Fruit("apple9", 9)],
#
#     [Fruit("apple10", 10), Fruit("orange3", 3), Fruit("orange5", 5), Fruit("banana10", 10), Fruit("apple4", 4),
#      Fruit("orange10", 10), Fruit("banana6", 6), Fruit("apple7", 7), Fruit("banana8", 8), Fruit("orange9", 9)]
# ]

#Case if all the fruits are already in the right basket
# randomBasket = [
#     [Fruit("apple1", 1), Fruit("apple2", 2), Fruit("apple3", 3), Fruit("apple10", 10), Fruit("apple7", 7),
#      Fruit("apple4", 4), Fruit("apple6", 6), Fruit("apple9", 9), Fruit("apple5", 5), Fruit("apple8", 8)],
#
#     [Fruit("orange2", 2), Fruit("orange5", 5), Fruit("orange1", 1), Fruit("orange3", 3), Fruit("orange10", 10),
#      Fruit("orange7", 7), Fruit("orange8", 8), Fruit("orange4", 4), Fruit("orange9", 9), Fruit("orange8", 8)],
#
#     [Fruit("banana2", 2), Fruit("banana5", 5), Fruit("banana1", 1), Fruit("banana3", 3), Fruit("banana10", 10),
#      Fruit("banana7", 7), Fruit("banana8", 8), Fruit("banana4", 4), Fruit("banana9", 9), Fruit("banana8", 8)]
# ]

#Case if all fruits are in the right order but random basket
# randomBasket = [
#     [Fruit("apple1", 1), Fruit("orange2", 2), Fruit("apple3", 3), Fruit("banana4", 4), Fruit("orange5", 5),
#      Fruit("banana6", 6), Fruit("apple7", 7), Fruit("apple8", 8), Fruit("orange9", 9), Fruit("orange10", 10)],
#
#     [Fruit("orange1", 1), Fruit("banana2", 2), Fruit("orange3", 3), Fruit("apple4", 4), Fruit("banana5", 5),
#      Fruit("orange6", 6), Fruit("banana7", 7), Fruit("orange8", 8), Fruit("apple9", 9), Fruit("banana10", 10)],
#
#     [Fruit("banana1", 1), Fruit("apple2", 2), Fruit("banana3", 3), Fruit("orange4", 4), Fruit("apple5", 5),
#      Fruit("apple6", 6), Fruit("orange7", 7), Fruit("banana8", 8), Fruit("banana9", 9), Fruit("apple10", 10)],
# ]

#Only the last item is misplaced
randomBasket = [
    [Fruit("apple1", 1), Fruit("apple2", 2), Fruit("apple3", 3), Fruit("apple4", 4), Fruit("apple5", 5),
     Fruit("apple6", 6), Fruit("apple7", 7), Fruit("apple8", 8), Fruit("apple9", 9), Fruit("banana10", 10)],

    [Fruit("banana1", 1), Fruit("banana2", 2), Fruit("banana3", 3), Fruit("banana4", 4), Fruit("banana5", 5),
     Fruit("banana6", 6), Fruit("banana7", 7), Fruit("banana8", 8), Fruit("banana9", 9), Fruit("orange10", 10)],

    [Fruit("orange1", 1), Fruit("orange2", 2), Fruit("orange3", 3), Fruit("orange4", 4), Fruit("orange5", 5),
     Fruit("orange6", 6), Fruit("orange7", 7), Fruit("orange8", 8), Fruit("orange9", 9), Fruit("apple10", 10)],
]

# All different ways to order the fruits
fruitOrdering = [["apple", "banana", "orange"], ["apple", "orange", "banana"],
                 ["banana", "apple", "orange"], [
                     "banana", "orange", "apple"],
                 ["orange", "apple", "banana"], ["orange", "banana", "apple"]]
