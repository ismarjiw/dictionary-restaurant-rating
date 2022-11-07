"""Restaurant rating lister."""


# put your code here
text = open('scores.txt')

list = []

dictionary = {}

for line in text:
    line = line.rstrip()
    words = line.split(':')
    list.append(words)

for restaurant in sorted(list):
    dictionary[restaurant[0]] = restaurant[1]
    print(f'{restaurant[0]} is rated at {restaurant[1]}.')

new_restaurant = input('Please add another restaurant name: ')
new_rating = input('What would you like to rate the restuarant? ')
dictionary[new_restaurant] = new_rating 

for restaurant, rating in dictionary.items():
    print(f'{restaurant} is rated at {rating}. ')














