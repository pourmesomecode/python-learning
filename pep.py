# Always use imports at the top of the file and drop two lines after to begin the programme
import sys
import os
# You can also import certain classes from modules like below
from MyModule import foo, bar, foobar


# visual indentation helps
def my_function(one, two,
                three, four,
                five, six):
    print("Hello World")


# two lines between top level functions and top level classes
def second_function():
    print("Second function")


my_list = [1,2,
           3,4,
           5,6]


check = True
if check is True:
    print("This is true")

# If statements should look like that above and not like...
if check is True: print("This is true")


# Calling multiple functions don't do the below
func one(); func_two(); func_three;
# Call them on a new line like..
func_one()
func_two()
func_three()

# Max line length should be 79 characters - Should already be set in PyCharm

# Over usage of white space - Example print( "test" ) remove the whitespace
# This is include for math operations also for example x = 3 * 3 + 5 * 2 would look like x = 3*3 + 5*2 since the
# addition sign has a lower priority so any whitespace should be added for the lower priority operation