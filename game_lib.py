#!/usr/bin/python3
#Alex Jordan
#1/28/2020

'''Creating a Media Database that holds and removes games from a database'''

import pickle
games = {}
def add_game():
    print("\nadd_game ran")
   
def print_all():
    key_list = games.keys()
       
    for key in key_list:
        print()
        print("Genre: ", games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("System: ", games[key][4])
        print("Release Date: ", games[key][5])
        print("Rating: ", games[key][6])
        print("Single/Multi: ", games[key][7])
        print("Beat the game?: ", games[key][8])    
        print("Purchase Date: ", games[key][9])
        print("Notes: ", games[key][10])
        print("----------------------")  
   

        
        
def remove_game():
    print("\nremove_game ran")
   
def save_data():
    datafile = open("game_lib.pickle", "wb")
    pickle.dump(games, datafile)
    datafile.close()
    print("Saved")
   
def quit():
    print("\nquit ran")
   
keep_going = True

datafile = open("game_lib.pickle", "rb")
games = pickle.load(datafile)
datafile.close()

 


def genre():
    genre = input("What is the Genre? ")
    for key in games.keys():
        entry = games[key]
        if genre == entry[0]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Beat the game?: ", entry[8])    
            print("Purchase Date: ", entry[9])
            print("Notes: ", entry[10])
            print("----------------------")    
            
def title():
    title = input("What is the Title? ")
    for key in games.keys():
        entry = games[key]
        if title == entry[1]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Beat the game?: ", entry[8])    
            print("Purchase Date: ", entry[9])
            print("Notes: ", entry[10])
            print("----------------------")                 

def developer():
    developer = input("Who is the Developer? ")
    for key in games.keys():
        entry = games[key]
        if developer == entry[2]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Beat the game?: ", entry[8])    
            print("Purchase Date: ", entry[9])
            print("Notes: ", entry[10])
            print("----------------------")  

def publisher():
    publisher = input("Who is the Publisher? ")
    for key in games.keys():
        entry = games[key]
        if publisher == entry[3]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Beat the game?: ", entry[8])    
            print("Purchase Date: ", entry[9])
            print("Notes: ", entry[10])
            print("----------------------")  

def system():
    system = input("What is the System? ")
    for key in games.keys():
        entry = games[key]
        if system == entry[4]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Beat the game?: ", entry[8])    
            print("Purchase Date: ", entry[9])
            print("Notes: ", entry[10])
            print("----------------------")  

def release():
    release = input("What is the Release Date? ")
    for key in games.keys():
        entry = games[key]
        if release == entry[5]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Beat the game?: ", entry[8])    
            print("Purchase Date: ", entry[9])
            print("Notes: ", entry[10])
            print("----------------------")  
            
def rating():
    rating = input("What is the Rating? ")
    for key in games.keys():
        entry = games[key]
        if rating == entry[6]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Beat the game?: ", entry[8])    
            print("Purchase Date: ", entry[9])
            print("Notes: ", entry[10])
            print("----------------------")  
            
def sing_multi():
    sing_multi = input("What is the Category? ")
    for key in games.keys():
        entry = games[key]
        if sing_multi == entry[7]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Beat the game?: ", entry[8])    
            print("Purchase Date: ", entry[9])
            print("Notes: ", entry[10])
            print("----------------------")  

def beat_game():
    beat_game = input("Have you beat the game? ")
    for key in games.keys():
        entry = games[key]
        if beat_game == entry[8]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Beat the game?: ", entry[8])    
            print("Purchase Date: ", entry[9])
            print("Notes: ", entry[10])
            print("----------------------")  

def purchase():
    purchase = input("When did you purchase it? ")
    for key in games.keys():
        entry = games[key]
        if purchase == entry[9]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Beat the game?: ", entry[8])    
            print("Purchase Date: ", entry[9])
            print("Notes: ", entry[10])
            print("----------------------")  
            
  
            

def search_games():
    print("\nsearch_games ran")
    print("Please select a search option")
    print('''
    1) Search by Genre:
    2) Search by Title:
    3) Search by Developer:
    4) Search by Publisher:
    5) Search by System:
    6) Search by Release Date:
    7) Search by Rating:
    8) Search by Category:
    9) Search by Games Beat:
    10) Search by Purchase Date:
   
    Q) Quit
    ''')
    

    choice = input("What would you like to select?: ")
    if choice == "1":
        genre()
    elif choice == "2":
        title()
    elif choice == "3":
        developer()
    elif choice == "4":
        publisher()
    elif choice == "5":
        system()
    elif choice == "6":
        release()
    elif choice == "7":
        rating()
    elif choice() == "8":
        sing_multi()
    elif choice() == "9":
        beat_game()
    elif choice() == "10":
        purchase()
    elif choice == "Q" or choice == "q":
        keep_going = False 

while keep_going:
    print("""
   
    MAIN MENU
    1) Add New Game
    2) Print All Games
    3) Search Game By Title
    4) Remove A Game
    5) Save Database
    6) Search for Games
   
   
    Q) Quit
   
    """)
   
    choice = input("What would you like to select?: ")
    if choice == "1":
        add_game()
    elif choice == "2":
        print_all()
    elif choice == "3":
        search_games()
    elif choice == "4":
        remove_game()
    elif choice == "5":
        save_data()
    elif choice == "6":
        search_games()
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
       
print("\nFarewell!.")    
