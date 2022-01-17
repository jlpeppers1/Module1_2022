"""
Program: main.py
Author: Joseph Peppers
Last date modified: 01/01/2022

The purpose of this program is convert age in years to months.
The input is an integer representing the age in years.
The output an integer representing the age in months.
"""

#This is a camment
print('Hello World!')

#I am going to set a name variable
users_name = 'Joe'

#Print out Hello to to the user's name
print('Hello' + ' ' + users_name + '. How are you?')
#Print out  the type of the name
print("The 'users_name' varialbe is type: " + str(type(users_name)))

#print("The 'users_name' varialbe is type: " + str(type(users_name)))
#print("The 'users_name' varialbe is type: " + str(<class 'str'>))
#print("The 'users_name' varialbe is type: " + "<class 'str'>")
#print("The 'users_name' varialbe is type: <class 'str'>")
#The 'users_name' varialbe is type: <class 'str'>

type_of_users_name = type(users_name)
str_of_type_of_users_name = str(type_of_users_name)
final_string = "The 'users_name' varialbe is type: " + str_of_type_of_users_name
print(final_string)
