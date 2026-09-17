# project-1 : 
## project-1 is a study on data structures:
we have a list of dictionaries each containing a
student's name and their grades, the code is designed 
to create and show:
1. The average grade of each student
2. The best score
3. All the grades combined
4. The best student's name and score


# project-2 :
## project-2 is a study on nested loops and while loops:
Using enumerate() to track both the index and value while looping through a list of lists, I calculated
the total inventory, counted empty slots, and found the position of the highest value in a warehouse dataset.
I also used a while loop with break and continue to handle repeated user input safely. 
The break statement lets me exit the loop when the user types "done", and continue lets me skip 
invalid input without crashing the program.


# project-3 :
## project-3 is a study on how to use *args and **kwargs in functions:
*args collects any number of positional arguments into a tuple, **kwargs collects any number of
keyword arguments into a dictionary. I practiced both by building a simple invoice function that combines 
regular parameters,*args, a default keyword argument, and **kwargs together.


# project-4 :
## project-4 is a study on how to manage exception errors:
I learned how to handle errors safely with try/except instead of letting the program crash.
I used ZeroDivisionError to catch division by zero, and ValueError to catch invalid (non-numeric) 
user input inside a while loop.


# CLI project:
## this project is comprehensive study on python basics:
I practiced these concepts on my own: 
Classes, functions and modules, loops and list comprehension, JSON storage,
how to create menus, user inputs and error handling, etc. to build a CLI for expense management.

[Files: expense.py, storage.py, main.py]


# Car class:
## this project is a simple (OOP) practice:
I created a Car class and developed it with heater and sensor as different classes using composition with a method called: (turn_heater_on), inside the method we use two other methods built inside Heater class.
the methods are designed to first turn the heater on(turn_on), then raise the temperature to the requested level(reach_requested_temp) 
and then shut down(turn_off).
the Sensor class has a method called (show), it generates a random number as a hypothetical temperature, we call this method 
inside (reach_requested_temp) and then assign it as the measured_temp.
So when you use the method(turn_heater_on) on an object from Car class(like c1):
It starts raising the generated number until it reaches the requested temperature(which is 25 by default), 
then it gets shut down through (turn_off) method.
