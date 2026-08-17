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
    for i, movies in enumerate(movie_genres[genre]):
        if movies == oldTitle:
            movie_genres[genre][i] = newTitle

def delete_movies(genre, title):
    if genre in movie_genres:
        if title in movie_genres[genre]:
            movie_genres[genre].remove(title)
                 

update_movies("Action", "Spiderman Brand new day", "Spiderman")
update_movies("Musical", "Mamma Mia", "The Greatest Showman")

print(movie_genres)

delete_movies("Sci-Fi", "Star wars")

print(movie_genres)

show_Movies()