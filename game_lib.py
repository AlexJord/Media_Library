#!/usr/bin/python3
#Alex Jordan
#1/28/2020

'''Creating a Media Database that holds and removes games from a database'''

import pickle
games = {}
def add_game():
    print("\nadd_game ran")
    new_key = len(games) + 1
    new_entry = []
    valid = False
    while not valid:
        #input stuff
        genre = input("What is the Genre?: ")
        new_entry.append(genre)
        title = input("What is the Title?: ")
        new_entry.append(title)
        developer = input("Who is the Developer?: ")
        new_entry.append(developer)
        publisher = input("Who is the Publisher?: ")
        new_entry.append(publisher)
        system = input("What is the System?: ")
        new_entry.append(system)
        release = input("When was the Release Date?: ")
        new_entry.append(release)   
        rating = input("What is the Rating?: ")
        new_entry.append(rating)        
        sing_multi = input("Is is Single or Multiplayer?: ")
        new_entry.append(sing_multi)        
        price = input("What is the Price?: ")
        new_entry.append(price)        
        beat_game = input("Have you Beat the Game?: ")
        new_entry.append(beat_game)        
        purchase = input("What is the date you purchased the game?: ")
        new_entry.append(purchase) 
        notes = input("Any Notes?: ")
        new_entry.append(notes)      
        answer = input("Is this correct?: ")
        valid = True
    games[new_key] = new_entry
    
    
def edit_game():
    print("Here is the Library: ")
    if key in games:
        valid = True
    else:
        games.pop()
    for key in games.keys():
        print(key, "-", games[key][1])
        
    edit_key = int(input("Which game do you want to edit?: "))        
    edit_entry = games[edit_key]
    print("Current Genre: ", edit_entry[0])
    print("Current Title: ", edit_entry[1])
    print("Current Developer: ", edit_entry[2])
    print("Current Publisher: ", edit_entry[3])
    print("Current System: ", edit_entry[4])
    print("Current Release Date: ", edit_entry[5])
    print("Current Rating: ", edit_entry[6])
    print("Current Single/Multiplayer choice: ", edit_entry[7])
    print("Current Price: ", edit_entry[8])
    print("Current status on beating the game: ", edit_entry[9])
    print("Current Purchase Date: ", edit_entry[10])
    print("Current Notes: ", edit_entry[11])
    edit_entry[0] = input("New Genre: ")
    edit_entry[1] = input("New Title: ")
    edit_entry[2] = input("New Developer: ")
    edit_entry[3] = input("New Publisher: ")
    edit_entry[4] = input("New System: ")  
    edit_entry[5] = input("New Release Date: ")
    edit_entry[6] = input("New Rating: ")
    edit_entry[7] = input("New Single or Multiplayer choice: ")
    edit_entry[8] = input("New Price: ")
    edit_entry[9] = input("Change if you beat the game: ")
    edit_entry[10] = input("New Purchase Date: ")
    edit_entry[11] = input("New Notes: ")
    
        
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
        print("Price: ", games[key][8])
        print("Beat the game?: ", games[key][9])    
        print("Purchase Date: ", games[key][10])
        print("Notes: ", games[key][11])
        print("----------------------")          
   
   

        
        
def remove_game():
    for key in games.keys():
        print(key, "-", games[key][1])    
   
    selected_key = input("What is the game you would like to delete?: ")
    
    try:
        selected_key = int(selected_key)
        confirm_deletion = input("Would you like to continue?: ")
        if confirm_deletion:
            for keys in range(1, len(games) + 1):
                if keys >= selected_key and keys != len(games):
                    games[keys] = games[keys + 1]
                else:
                    if keys == len(games):
                        games.pop(keys)
    except Exception as e:
        print("Failure to remove game")
        print(e)
    
    
   
def save_data():
    datafile = open("game_lib.pickle", "wb")
    pickle.dump(games, datafile)
    datafile.close()
    print("Saved")
   
def quit():
    print("Quit ran")
    quit = input("Would you like to save the database? (y/n): ")
    if quit == "y":
        datafile = open("game_lib.pickle", "wb")
        pickle.dump(games, datafile)
        datafile.close()
        print("Saved")
            
        
    exit()
   
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
            print("Price: ", entry[8])
            print("Beat the game?: ", entry[9])    
            print("Purchase Date: ", entry[10])
            print("Notes: ", entry[11])
            print("----------------------")                
          
        else:
            print("Oops, not found!")
            
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
            print("Price: ", entry[8])
            print("Beat the game?: ", entry[9])    
            print("Purchase Date: ", entry[10])
            print("Notes: ", entry[11])
            print("----------------------")                             
       
        else:
            print("Oops, not found!")       


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
            print("Price: ", entry[8])
            print("Beat the game?: ", entry[9])    
            print("Purchase Date: ", entry[10])
            print("Notes: ", entry[11])
            print("----------------------")   
        
        else:
            print("Oops, not found!")            

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
            print("Price: ", entry[8])
            print("Beat the game?: ", entry[9])    
            print("Purchase Date: ", entry[10])
            print("Notes: ", entry[11])
            print("----------------------")              

        else:
            print("Oops, not found!")

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
            print("Price: ", entry[8])
            print("Beat the game?: ", entry[9])    
            print("Purchase Date: ", entry[10])
            print("Notes: ", entry[11])
            print("----------------------")    
            
        else:
            print("Oops, not found!")            

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
            print("Price: ", entry[8])
            print("Beat the game?: ", entry[9])    
            print("Purchase Date: ", entry[10])
            print("Notes: ", entry[11])
            print("----------------------")  
            
        else:
            print("Oops, not found!")            
            
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
            print("Price: ", entry[8])
            print("Beat the game?: ", entry[9])    
            print("Purchase Date: ", entry[10])
            print("Notes: ", entry[11])
            print("----------------------")   
            
        else:
            print("Oops, not found!")            
            
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
            print("Price: ", entry[8])
            print("Beat the game?: ", entry[9])    
            print("Purchase Date: ", entry[10])
            print("Notes: ", entry[11])
            print("----------------------")   
            
        else:
            print("Oops, not found!")            
            
def price():
    price = input("What is the Price? ")
    for key in games.keys():
        entry = games[key]
        if price == entry[8]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Price: ", entry[8])
            print("Beat the game?: ", entry[9])    
            print("Purchase Date: ", entry[10])
            print("Notes: ", entry[11])
            print("----------------------") 
            
        else:
            print("Oops, not found!")            

def beat_game():
    beat_game = input("Have you beat the game? ")
    for key in games.keys():
        entry = games[key]
        if beat_game == entry[9]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Price: ", entry[8])
            print("Beat the game?: ", entry[9])    
            print("Purchase Date: ", entry[10])
            print("Notes: ", entry[11])
            print("----------------------") 
            
        else:
            print("Oops, not found!")            

def purchase():
    purchase = input("When did you purchase it? ")
    for key in games.keys():
        entry = games[key]
        if purchase == entry[10]:
            print()
            print("Genre: ", entry[0])
            print("Title: ", entry[1])
            print("Developer: ", entry[2])
            print("Publisher: ", entry[3])
            print("System: ", entry[4])
            print("Release Date: ", entry[5])
            print("Rating: ", entry[6])
            print("Single/Multi: ", entry[7])
            print("Price: ", entry[8])
            print("Beat the game?: ", entry[9])    
            print("Purchase Date: ", entry[10])
            print("Notes: ", entry[11])
            print("----------------------")  
            
        else:
            print("Oops, not found!")            
            
  
            

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
    9) Search by Price:
   10) Search by Games Beat:
   11) Search by Purchase Date:
   
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
    elif choice == "8":
        sing_multi()
    elif choice == "9":
        price()
    elif choice == "10":
        beat_game()
    elif choice == "11":
        purchase()
    elif choice == "Q" or choice == "q":
        keep_going = False 

while keep_going:
    print("""
   
    MAIN MENU
    1) Add New Game
    2) Edit Game
    3) Print All Games
    4) Search Game By Title
    5) Remove A Game
    6) Save Database
    7) Search for Games
   
   
    Q) Quit
   
    """)
   
    choice = input("What would you like to select?: ")
    if choice == "1":
        add_game()
    elif choice == "2":
        edit_game()
    elif choice == "3":
        print_all()
    elif choice == "4":
        search_games()
    elif choice == "5":
        remove_game()
    elif choice == "6":
        save_data()
    elif choice == "7":
        search_games()
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
       
print("\nFarewell!.")    
