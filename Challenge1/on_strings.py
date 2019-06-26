#This file will teach you the basics of strings in Python. Feel free to execute the script by 
#right clicking then selecting the option 'Run python file in terminal'

#Strings are sequences of characters enclosed in quotes 'string' or double quotes "string"

print('This is a string') #The "print" method simply prints a string to the console.

#A string can be stored in a variable like this:

var = 'This is a string stored in a variable'

#or like this:

var2 = 'This is a second string'

#and since the variable "var" contains a string then it can be printed as well:

print(var)

#you can concatenate (put together) strings by using the plus '+' symbol

print('I am concatenating a string ' + var)

#the "print" method will print a string in a new line each time you use it, if you want to avoid that use the following:
print('This string will be printed in a new line', end='') #We added a new argument to the function 'print',
#this argument simply tells the method 'print' that we will not put a new line character at the end.
print('This string will be printed in the same line as last one') 

#A new line character is expressed as '\n'
print('one\nnew\nline\neach\ntime') #This string will print each word in a different line because of the
#new line characters. By default the 'print' method assumes the last character is '\n' if the 'end=' argument is not specified.

#There are other special characters like '\t' for tabs.
print('one\tnew\ttab\teach\ttime')

#Since strings are sequence of characters then you can select and 'slice' a string:
#you do it like this:
print(var[0]) #this will print the first character in the string inside var. The number is an index, it starts from 0. Like so 0,1,2,3,4,5...
print(var[1]) #this will print the second character. Sort of confusing.
print(var[1:4]) #this will print the second character up until the fourth

#You can combine the functionality.
print('\nthis is combined' + ' functionality \n' + var[1:10])

#Please keep experimenting with strings and move on to the challenge.



