# Other needed Functions

from os import system, name # import some functions like clear screen etc

def clear():  # special function for clear screen

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
