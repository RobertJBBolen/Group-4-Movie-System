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

    for movie in movies:
        if keyword in movie["title"].lower() or keyword in movie["genre"].lower():
            print(f"\nTitle: {movie['title']}")
            print(f"Genre: {movie['genre']}")
            found = True

    if not found:
        print("\nNo movies found.")

    input("\nPress Enter to return to main menu...")