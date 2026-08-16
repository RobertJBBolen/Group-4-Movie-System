genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Fantasy", "Romance", "Thriller"]
width = 60

def banner():

    print("="*width+"\n")
    print(" "+"🎬 WELCOME 🎬".center(width)+" \n")
    print(" "+"S C R E E N S P A C E".center(width)+" \n")
    print(" "+"YOUR WORLD OF MOVIES STARTS HERE".center(width)+" \n")
    print("="*width+"\n")

    print("  Welcome to ScreenSpace! \n")
    print("  Explore movies, discover recommendations, search for \n    your favorite films, and learn more about the stories \n    and characters behind them. \n")
    print("  Share your thoughts through reviews and discover something \n    new every time you visit. \n")

    print("="*width+"\n")
    print(" "+"[1] Register".center(width)+" ")
    print(" "+"[2] Exit".center(width)+" ")
    print("="*width+"\n")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        register()
    elif choice == 2:
        False
    else:
        print("Invalid Input")
        return

def register():
    print("="*20 + " REGISTER " + "="*20)
    
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    print(genres)
    favGenre = input("Enter your Favorite Genre: ")

def menu():
    while True:
        print()
        print("="*width)
        print(""+"MAIN MENU".center(width)+"")
        print("="*width)
        print("\n [1] Suggested Movies\n [2] Search Movies\n [3] Add Movie\n [4] Update Movie\n [5] Delete Movie\n [6] Profile\n [7] Exit\n  ")
        print("="*width)

        choice = int(input("Enter your choice: "))
            
        if choice == 1:
            print("\nOpening suggested movie...")
            suggested()
        elif choice == 2:
            print("\nOpening search movie...")
            search()
        elif choice == 3:
            print("\nOpening add movie...")
            addMovie()
        elif choice == 4:
            print("\nOpening update movie...")
            updateMovie()
        elif choice == 5:
            print("\nOpening delete movie...")
            deleteMovie()
        elif choice == 6:
            print("\nOpening profile...")
            profile(user)
        elif choice == 7:
            print("\nThank you for using screenspace")
            break
        else:
            print("\nInvalid choice")
    
menu()