#!/usr/bin/python3
#Alex Jordan
#1/28/2020

'''Creating a Media Database that holds and removes games from a database'''


def print_all(sort_it=False):
    print("Ran print_all()")

def lookup():
    print("Ran lookup()")
        
        
def add_edit():
    print("Ran add_edit()")
        
def remove_game():
    print("Ran remove_game()")
        
def lookup_by_title():
    print("Ran lookup_by_title()")
        
def quit():
    #print("running quit()")  
    print("Ran quit()")
    exit()





while True:
    print("""
    Welcome to Media Library.
    ---------------------------
    
    MAIN MENU
    1) Add/Edit Games
    2) Print All Games
    3) Search by Title
    4) Remove a game
    5) Save Database
 
    Q) Quit
    """)
    choice = input("What option would you like? ") 
    
    if choice == "1":
        add_edit()
    elif choice == "2":
        print_all()
    elif choice == "3":
        lookup_by_title()
        
    elif choice == "4":
        remove_game()
        
    elif choice == "5":
        print_all(sort_it = True)
        
    
        
    
        
    elif choice == "Q" or choice == "q":
        quit()
    else:
        print("*** NOT A VALID CHOICE ***\n")
    
print("Oh MY! Something really went wrong!")