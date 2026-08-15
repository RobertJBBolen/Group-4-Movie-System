genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Fantasy", "Romance", "Thriller"]

def banner():
    width = 60

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

banner()