
#import modules
import random

name = "Sam"
weight = 198.7
age = 67
is_cool = True

print "my name is " + name + " I am " + str(age) + " years old"

a_list = []
a_list.append("the first thing")

print a_list

# make a list
a_list.append("the second thing")
a_list.append("the third thing")
a_list.append("the fourth thing")
a_list.append("the fifth thing")
a_list.append("the sixth thing")


# print a list
# print a_list[2]
# print a_list[-1]

for item in a_list:
    print item

some_numbers = [100,121,2,332,64,-3000,30]

for number in some_numbers:
    print number
    if number > 0:
        print "the number is bigger than 0"
    else: 
        print "that number is less than 0!"

def say_hi(name):
    print "hello " + name + "!!!"

say_hi("Marx")

print random.randint(100,1000)
