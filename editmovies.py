from movies import movies

def update_movies():
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
            print(f"Successfully updated '{oldTitle}' to '{newTitle}'.")
        else:
            print(f"Error: Could not find '{oldTitle}' in '{genre}'.")
    else:
        print(f"Error: Genre '{genre}' does not exist.")

def delete_movies():
    genre = input("Enter genre to delete from: ")

    if genre in [m["genre"] for m in movies]:
        title = input("Enter movie title to delete: ")

        movie_found = None
        for m in movies:
            if m["genre"] == genre and m["title"] == title:
                movie_found = m
                break

        if movie_found:
            movies.remove(movie_found)
            print(f"Successfully deleted '{title}'.")
        else:
            print(f"Error: Could not find '{title}' in '{genre}'.")
    else:
        print(f"Error: Genre '{genre}' does not exist.")
