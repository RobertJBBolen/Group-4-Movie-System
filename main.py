from movie import movies, getGenre
from add_movie import addMovie
from recommend_movie import recommend
from editmovies import *
from review import *
from read import search

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

def register():
    print("\n"+"="*20 + " REGISTER " + "="*20+"\n")

    while True:
        name = input("Enter your name: ")

        if name == "":
            print("\nName cannot be empty.")
        elif any(char.isdigit() for char in name):
            print("\nName cannot contain numbers.")
        else:
            break

    while True:
        try:
            age = int(input("\nEnter your age: "))

            if 1 <= age <= 120:
                break
            else:
                print("\nPlease enter an age between 1 and 120.")

        except ValueError:
            print("\nInvalid input. Please enter numbers only.")

    print()
    print("\nGenres:")

    genres = getGenre()

    for i, genre in enumerate(genres, 1):
        print(f"[{i}] {genre}")

    while True:
        try:
            choices = input("\nEnter your Favorite Genres (example: 1 3 5): ").split()

            choices = [int(choice) for choice in choices]

            if all(1 <= choice <= len(genres) for choice in choices):
                choices = list(set(choices))
                break
            else:
                print(f"Please enter numbers from 1 to {len(genres)}.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    favGenre = [genres[choice - 1] for choice in choices]

    print("\nRegistration Complete!\n")

    return{
        "name": name,
        "age": age,
        "favGenre": favGenre
    }

def menu(user):
    while True:
        print()
        print("="*width)
        print(""+"MAIN MENU".center(width)+"")
        print("="*width)
        print("\n [1] Recommendation Movies\n [2] Search Movies\n [3] Add Movie\n [4] Review Movie\n [5] Update Movie\n [6] Delete Movie\n [7] Profile\n [8] Exit\n  ")
        print("="*width)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            continue
            
        if choice == 1:
            print("\nOpening recommendation movie...")
            recommend(user)
        elif choice == 2:
            print("\nOpening search movie...")
            search()
        elif choice == 3:
            print("\nOpening add movie...")
            addMovie()
        elif choice == 4:
            print("\nOpening add reviews...")
            addReview()
        elif choice == 5:
            print("\nOpening update movie...")
            updateMovie()
        elif choice == 6:
            print("\nOpening delete movie...")
            deleteMovie()
        elif choice == 7:
            print("\nOpening profile...")
            profile(user)
        elif choice == 8:
            print("\nThank you for using screenspace")
            return False
        else:
            print("\nInvalid choice\n")

def profile(user):
    print("="*width)
    print(""+"Profile".center(width)+"")
    print("="*width)
    print(f"\nName             : {user['name']}")
    print(f"Age              : {user['age']}")
    print(f"Favorite Genre   : {user['favGenre']}")
    print()
    print("="*width)

    input("Press Enter to return to main menu...")
    
def main():
    while True:
        banner()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            continue

        if choice == 1:
            user = register()
            input("Press ENTER to continue")
            running = menu(user)

            if running == False:
                break
        elif choice == 2:
            print("\nThank you for using screenspace")
            break
        else:
            print("\nInvalid Input\n")
            
if __name__ == "__main__":
    main()

    
