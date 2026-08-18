from movie import movies


def show_Movies():

    print("=" * 50)

    if not movies:
        print("No movies found in the library.")
        print("=" * 50)
        return

    genres = {}

    for movie in movies:
        genre = movie["genre"]

        if genre not in genres:
            genres[genre] = []

        genres[genre].append(movie)

    number = 1

    for genre, movie_list in genres.items():
        print(f"\nGenre: {genre}")

        for movie in movie_list:
            print(f"[{number}] {movie['title']}")
            number += 1

    print("=" * 50)


def updateMovie():

    if not movies:
        print("No movies available to update.")
        return

    show_Movies()

    while True:
        try:
            choice = int(
                input("\nEnter the number of the movie to update: ")
            )

            if 1 <= choice <= len(movies):
                movie_found = movies[choice - 1]
                break
            else:
                print(
                    f"Please enter a number from 1 to {len(movies)}."
                )

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    print(f"\nSelected movie: {movie_found['title']}")

    newTitle = input("Enter new title: ").strip()

    if newTitle == "":
        print("Movie title cannot be empty.")
        return

    newGenre = input("Enter new genre: ").strip()

    if newGenre == "":
        print("Movie genre cannot be empty.")
        return

    while True:
        try:
            newYear = int(
                input("Enter new release year: ")
            )

            if 1888 <= newYear <= 2100:
                break

            print("Please enter a valid year.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    newDescription = input(
        "Enter new description: "
    ).strip()

    if newDescription == "":
        print("Movie description cannot be empty.")
        return

    oldTitle = movie_found["title"]

    movie_found["title"] = newTitle
    movie_found["genre"] = newGenre
    movie_found["year"] = newYear
    movie_found["description"] = newDescription

    print(
        f"\nSuccessfully updated "
        f"'{oldTitle}' to '{newTitle}'!"
    )


def deleteMovie():

    if not movies:
        print("No movies available to delete.")
        return

    show_Movies()

    while True:
        try:
            choice = int(
                input("\nEnter the number of the movie to delete: ")
            )

            if 1 <= choice <= len(movies):
                movie_to_delete = movies[choice - 1]
                break
            else:
                print(
                    f"Please enter a number from 1 to {len(movies)}."
                )

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    print(
        f"\nSelected movie: {movie_to_delete['title']}"
    )

    while True:
        confirm = input(
            "Are you sure you want to delete this movie? (yes/no): "
        ).strip().lower()

        if confirm in ["yes", "y"]:
            movies.remove(movie_to_delete)

            print(
                f"\nSuccessfully deleted "
                f"'{movie_to_delete['title']}'."
            )
            break

        elif confirm in ["no", "n"]:
            print("\nDeletion cancelled.")
            break

        else:
            print("Please enter yes or no.")
