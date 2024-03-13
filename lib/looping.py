#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i <=10:
        print(i)
        i -= 1
        if i == 0:
            print('Happy New Year!')
            break

def square_integers(int_list):
    squared_numbers = [i**2 for i in int_list if isinstance(i, int)]
    return squared_numbers


def fizzbuzz():
    i = 1
    while i<=100 :
       if i % 3 == 0 and i % 5 == 0:
           print(f'FizzBuzz')
       elif i % 3 == 0:
           print(f'Fizz')
       elif i % 5 == 0:
           print(f'Buzz')
       else:
           print(i)
       i += 1
           



new_year = happy_new_year

print(new_year)