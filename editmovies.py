from movie import movies


def show_Movies():

    print("=" * 50)

    if not movies:
        print("No movies found in the library.")
        print("=" * 50)
        return

    genres = {}

    for m in movies:
        genre = m["genre"]

        if genre not in genres:
            genres[genre] = []

        genres[genre].append(m)

    for genre, movie_list in genres.items():

        print(f"\nGenre: {genre}")

        for i, movie in enumerate(movie_list, 1):
            print(f"[{i}] {movie['title']}")

    print("=" * 50)


def updateMovie():

    show_Movies()

    genre = input("Enter genre to update: ").strip()

    genre_movies = [
        m for m in movies
        if m["genre"].lower() == genre.lower()
    ]

    if not genre_movies:
        print(f"Error: Genre '{genre}' does not exist.")
        return

    print(f"\nMovies in {genre}:")

    for i, movie in enumerate(genre_movies, 1):
        print(f"[{i}] {movie['title']}")

    while True:
        try:
            choice = int(
                input("\nEnter movie number to update: ")
            )

            if 1 <= choice <= len(genre_movies):
                movie_found = genre_movies[choice - 1]
                break

            print(
                f"Please enter a number from 1 "
                f"to {len(genre_movies)}."
            )

        except ValueError:
            print("Invalid input. Please enter a number.")

    oldTitle = movie_found["title"]

    newTitle = input("Enter new title: ").strip()

    if newTitle == "":
        print("Movie title cannot be empty.")
        return

    new_genre = input(
        "Enter new genre: "
    ).strip()

    if new_genre == "":
        print("Movie genre cannot be empty.")
        return

    while True:
        try:
            new_year = int(
                input("Enter new release year: ")
            )

            if 1888 <= new_year <= 2100:
                break

            print("Please enter a valid year.")

        except ValueError:
            print(
                "Invalid year. Please enter numbers only."
            )

    new_desc = input(
        "Enter new description: "
    ).strip()

    if new_desc == "":
        print("Movie description cannot be empty.")
        return

    movie_found["title"] = newTitle
    movie_found["genre"] = new_genre
    movie_found["year"] = new_year
    movie_found["description"] = new_desc

    print(
        f"\nSuccessfully updated "
        f"'{oldTitle}' to '{newTitle}'!"
    )

    print("Existing rating and reviews were preserved.")


def deleteMovie():

    show_Movies()

    genre = input(
        "Enter genre to delete from: "
    ).strip()

    genre_movies = [
        m for m in movies
        if m["genre"].lower() == genre.lower()
    ]

    if not genre_movies:
        print(
            f"Error: Genre '{genre}' does not exist."
        )
        return

    print(f"\nMovies in {genre}:")

    for i, movie in enumerate(genre_movies, 1):
        print(f"[{i}] {movie['title']}")

    while True:
        try:
            choice = int(
                input("\nEnter movie number to delete: ")
            )

            if 1 <= choice <= len(genre_movies):
                movie_to_delete = genre_movies[
                    choice - 1
                ]
                break

            print(
                f"Please enter a number from 1 "
                f"to {len(genre_movies)}."
            )

        except ValueError:
            print("Invalid input. Please enter a number.")

    title = movie_to_delete["title"]

    confirm = input(
        f"Are you sure you want to delete "
        f"'{title}'? (yes/no): "
    ).strip().lower()

    if confirm in ["yes", "y"]:
        movies.remove(movie_to_delete)
        print(
            f"Successfully deleted '{title}'."
        )
    else:
        print("Deletion cancelled.")
