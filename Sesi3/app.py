def penjumlahan(num1, num2, num3):
    '''Function to calculate area of a square'''
    return num1 + num2 + num3

def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)


def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
   

my_function(9, 10)
print(my_function.__doc__)

printme("hello")

hasil= penjumlahan(2,34,1)
print(f"Hasil penjumlahan adalah : {hasil}")

# Function definition is here
def printinfo( arg1, *vartuple ):
# def printinfo(arg1, arg2, arg3, arg4):
   '''This prints a variable passed arguments'''
   print('arg1     : ', arg1)
   print('vartuple : ', vartuple)
   print('')
   
   for var in vartuple:
      print('isi vartuple : ', var) 

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )


def person_car(total_data, **kwargs):
  '''Create a function to print who owns what car'''
  print('Total Data : ', total_data)
  for key, value in kwargs.items():
    print('Person : ', key)
    print('Car    : ', value)
    print('')

person_car(4, jimmy='chevrolet', frank='ford', tina='honda')
person_car(3)


sum = lambda arg1, arg2: arg1 + arg2

# That lambda function will be equal to :
# def sum(arg1, arg2):
#     return arg1+arg2

# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))
print('')

#import sys
# print(sys.path)
#sys.path.append(r'C:\Users\yosia\OneDrive\Documents\OCBC NISP\Bootcamp 2\H8py')
from H8py2.person import name,devices, display as display_person

print(name)
print(devices)
display_person("Hello")
print(dir())
print('')

import brands
import importlib
print(importlib.reload(brands))
print('')

# import pkg.mod1, pkg.mod2
# print(pkg.mod1.kitchen_sets)
# print(pkg.mod2.artist_kits)
from pkg.mod1 import kitchen_sets as ks
print(ks)
print('')