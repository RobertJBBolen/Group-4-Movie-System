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
        title = m["title"]
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(title)

    for genre, movie_list in genres.items():
        print(f"Genre: {genre} Movies: {movie_list}")

    print("=" * 50)

def updateMovie():
    show_Movies()
    genre = input("Enter genre to update: ")

    if genre in [m["genre"] for m in movies]:
        oldTitle = input("Enter old title: ")

        movie_found = None
        for m in movies:
            if m["genre"] == genre and m["title"] == oldTitle:
                movie_found = m
                break

        if movie_found:
            newTitle = input("Enter new title: ")
            movie_found["title"] = newTitle

            try:
                new_year = int(input("Enter new release year: "))
                movie_found["year"] = new_year
            except ValueError:
                print("Invalid year entered. Keeping original year.")

            new_desc = input("Enter new description: ")
            if new_desc.strip():
                movie_found["description"] = new_desc

            movie_found["rating"] = None  
            movie_found["reviews"] = []  
            print(
                f"\nSuccessfully updated '{oldTitle}' to '{newTitle}'!"
            )
            print("Rating reset to None and reviews cleared for updated movie.")
        else:
            print(f"Error: Could not find '{oldTitle}' in '{genre}'.")
    else:
        print(f"Error: Genre '{genre}' does not exist.")


def deleteMovie():
    show_Movies()
    genre = input("Enter genre to delete from: ")

    if genre in [m["genre"] for m in movies]:
        title = input("Enter movie title to delete: ")

        movie_to_delete = None
        for m in movies:
            if m["genre"] == genre and m["title"] == title:
                movie_to_delete = m
                break

        if movie_to_delete:
            movies.remove(
                movie_to_delete
            )
            print(f"Successfully deleted '{title}'.")
        else:
            print(f"Error: Could not find '{title}' in '{genre}'.")
    else:
        print(f"Error: Genre '{genre}' does not exist.")

