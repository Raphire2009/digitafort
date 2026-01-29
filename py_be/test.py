"""
# Python with Databases: Interacting with SQLite using `sqlite3`

This file provides a guide to using Python's built-in `sqlite3` module to work
with SQLite databases. SQLite is a lightweight, serverless, file-based database,
which makes it incredibly easy to get started with databases in Python.
"""

#import sqlite3
#import os


#DB_FILE = "example.db"


#todo
# check if file exist 
# clean the old db 
#if os.path.exists(DB_FILE):
#    os.remove(DB_FILE)

#erro check 
#connect 
#try:
#    connect_db = sqlite3.connect(DB_FILE)
#except sqlite3.DatabaseError as e:
#    print(f"failed{e}")


#name = int(input("Your Age :"))
#print(name)

#import tkinter as tk 

#root = tk.Tk()
#root.title(" My app")


#root.mainloop()



#string
#int
#float
#bool


#kkkkkkkkkkk
"""
kkkkkkkkkkk
"""

#create 2 a var 
# add the value 
# substract them 
# **
# * 


#a = 8 # attend classes
#b = 3 # read your books
#c = 6 # don't attend 
#d = 4

#passing  =  (a > 3) or (c < d)
#print(passing)


#name = 40 
#name -= name 


#if you came to class -> if you came with your system   -> learn 
#else ->dont learn 

a = 2
b = 3
c,d = a,b 




#position , apple = en(0,apple)

#0, apple
#en(0,apple ) = [
#  0 : apple
# ]
#       0       1         2


#





          
fruits = ["apple","orange"]
fruits.append("mango")
fruits.append(9.333)
fruits[2] = "banana"
fruits.remove(9.333)
fruits.append("apple")



#print(f"this are the item: {item}", type(item))

#                0,1,2, 3
mutable_tuple = (1,2,3, [4,5,6])
mutable_tuple[3][0] = 89

number =  (1,2,3,3,4,5,6)
first , *second, last  = number 
#print(first, *second, last)



def get_more_value():
    return "alice", 30, "example@gmail.com"


name, age , mail = get_more_value()
#print(name,age,mail)



location  = {
    (40.7128, -74.0060): "New York City",
    (34.0522, -118.2437): "Los Angeles"
}

import sys


num_l = [1,2,3,4,5]
#print("List size in bytes :",sys.getsizeof(num_l))
num_t = (1,2,3,4,5)
#print("Turple Size i Bytes: ", sys.getsizeof(num_t))

from collections import namedtuple

Point = namedtuple('Point',['x','y','z'])


anything = { "name": "victor", "age" : 92,  "location":"UK" }

print(anything['name'])

