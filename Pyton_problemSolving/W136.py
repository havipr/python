from PyTest import *
##////////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Write Python code that reads a boolean and an integer from the keyboard.   //
## If the boolean is True and the integer is in the range 1. . 100 OR if      //
## the boolean is False and the integer is not in the range 1..100 and the    //
## integer is not in the range -20..-8 print True. Otherwise print False.     //
## You must not use the Python if or if-else statement.                       //
##                                                                            //
## All ranges are inclusive                                                   //
##                                                                            //
## Example inputs/outputs are:                                                //
##    True 50   -> True                                                       //
##    True -5   -> False                                                      //
##    False 50  -> False                                                      //
##    False 200 -> True                                                       //
##    False -5  -> True                                                       //
##//////////////////////////////////////////////////////////////////////////////

a = input('Pls write a boolean: ').capitalize()
b = input('Pls write an integer: ')
c = False

while a == 'True' and b in range(1,101):
    c = True
    break
while a =='False' and b not in range(-20,-7) and b not in range(1,101):
    c = True
    break

print(c)
