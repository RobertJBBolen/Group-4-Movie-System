movie_genres = {"Action": ["Spiderman Brand new day"],
            "Musical": ["Mamma Mia"],
            "Comedy": ["Mean Girls"],
            "Sci-Fi": ["Star wars"]
}

def show_Movies():
    print("=" * 50)
    for genre, movies in movie_genres.items():
        print(f"Genre: {genre} Movie: {movies}")
    print("=" * 50)

show_Movies()

def update_movies(genre, oldTitle, newTitle):
    if genre in movie_genres:
        if oldTitle in movie_genres[genre]:
            for i, movies in enumerate(movie_genres[genre]):
                if movies == oldTitle:
                    movie_genres[genre][i] = newTitle
            print(f"Successfully updated '{oldTitle}' to '{newTitle}'.")
        else:
            print(f"Error: Could not find '{oldTitle}' in '{genre}'.")
    else:
        print(f"Error: Genre '{genre}' does not exist.")

def delete_movies(genre, title):
    if genre in movie_genres:
        if title in movie_genres[genre]:
            movie_genres[genre].remove(title)
            print(f"Successfully deleted '{title}'.")
        else:
            print(f"Error: Could not find '{title}' in '{genre}'.")
    else:
        print(f"Error: Genre '{genre}' does not exist.")

# pang test lang to sa mga functions
genre = input("Enter genre to update: ")
old_title = input("Enter old title: ")
new_title = input("Enter new title: ")
update_movies(genre, old_title, new_title)

show_Movies()

del_genre = input("Enter genre to delete from: ")
del_title = input("Enter movie title to delete: ")
delete_movies(del_genre, del_title)

show_Movies()
