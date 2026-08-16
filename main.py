#MAIN (user login, UI and such here)

# Features

# CREATE / (Add Movies (Genre, Title))

# READ / (Search movies(Genre -> Movie), Show Reviews and comments etc.)

# UPDATE / (Updating Movie titles & managing movies.)

# DELETE / (Delete movies)

movie_genres = {
    "Action": ["Spiderman Brand new day"],
    "Musical": ["Mamma Mia"],
    "Comedy": ["Mean Girls"],
    "Sci-Fi": ["Star wars"]
}

def search():
    print("\nSEARCH MOVIES\n")

    keyword = input("Enter movie title or genre: ").strip().lower()
    found = False

    for genre, titles in movie_genres.items():
        for title in titles:
            if keyword in title.lower() or keyword in genre.lower():
                print(f"\nTitle: {title}")
                print(f"Genre: {genre}")
                found = True

    if not found:
        print("\nNo movies found.")

    input("\nPress Enter to return to main menu...")

search()