from movie import movies, getGenre

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
        print("\n [1] Recommendation Movies\n [2] Search Movies\n [3] Add Movie\n [4] Update Movie\n [5] Delete Movie\n [6] Profile\n [7] Exit\n  ")
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
            return False
        else:
            print("\nInvalid choice\n")

def recommend(user):
    print("=" * width)
    print("Recommend Movies".center(width))
    print("=" * width)

    recommended_movies = []

    for movie in movies:
        if movie["genre"] in user["favGenre"]:
            recommended_movies.append(movie)

    if not recommended_movies:
        print("\nNo movies found for your favorite genres.")
        print("=" * width)
        input("Press Enter to return to main menu...")
        return

    print("\nMovies recommended for you:\n")

    for i, movie in enumerate(recommended_movies, 1):
        print(f"[{i}] {movie['title']}")
        print(f"    Genre  : {movie['genre']}")
        print(f"    Rating : {movie['rating']}")
        print()

    while True:
        try:
            choice = int(input("Enter the movie number to view details: "))

            if 1 <= choice <= len(recommended_movies):
                selected_movie = recommended_movies[choice - 1]

                print("\n" + "=" * width)
                print("MOVIE DETAILS".center(width))
                print("=" * width)

                print(f"\nTitle       : {selected_movie['title']}")
                print(f"Genre       : {selected_movie['genre']}")
                print(f"Year        : {selected_movie['year']}")
                print(f"Rating      : {selected_movie['rating']}")
                print(f"Description : {selected_movie['description']}")

                print("\n" + "=" * width)

                input("Press Enter to return to main menu...")
                break

            else:
                print(f"Please enter a number from 1 to {len(recommended_movies)}.")

        except ValueError:
            print("Invalid input. Please enter a number.")

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
            
main()

    