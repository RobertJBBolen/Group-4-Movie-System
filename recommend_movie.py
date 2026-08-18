from movie import movies, getGenre

width = 60

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