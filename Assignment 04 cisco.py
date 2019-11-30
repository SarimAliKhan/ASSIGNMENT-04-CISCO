#QS1
dic = {'first name' : 'sarim','last name' : 'ali khan','age': 20,'city' : 'karachi'}
print(dic)
dic['qualification'] = 'university'
print(dic)
d1 = {'qualification':'high academic level'}
dic.update(d1)
print(dic)
dic.popitem()
print(dic)

#QS2

cities = {'Karachi' : {'country' : 'Pakistan','population' : '20mil','fact' :'bryani is too good'},
          'Mexico': {'country': 'Mexico', 'population': '200mil', 'fact': 'pasta is too good'},
          'dehli': {'country': 'India', 'population': '10mil', 'fact': 'nehari is too good'}}
print(cities['Karachi'])
print(cities['Mexico'])
print(cities['dehli'])

#QS3
age = int(input('Enter your age :'))
if age < 3:
    print('ticket is free')
elif age in range(3,12):
    print('ticket is 10$')
elif age > 12:
    print('ticket is 15$')

#QS4
def favourite_book(title):
    print('My favourite book is',title)

favourite_book('harry potter')

#QS5
import random
ran = random.randrange(1,30)
count = 0
while count < 3:
    guess = int(input('Enter your guess number:'))
    count += 1
    if guess > ran:
        print('number you guessed is greater than the guessing number')
        #count += 1
        #guess = int(input('Enter your guess name:'))

    elif guess < ran:
        print('number you guessed is smaller than the guessing number')
        #count += 1
        #guess = int(input('Enter your guess name:'))
    elif guess == ran:
        print('the number you guesses is right')
        #count +=1
        #guess = int(input('Enter your guess name:'))



