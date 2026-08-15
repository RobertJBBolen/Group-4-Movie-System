movie_genres = {"Action": ["Spiderman Brand new day"],
            "Musical": ["Mamma Mia"],
            "Comedy": ["Mean Girls"],
            "Sci-Fi": ["Star wars"]
}

def show_Movies():
    print("=" * 30)
    for genre, movies in movie_genres.items():
        print(f"Genre: {genre} Movie: {movies}")

show_Movies()

def update_movies(genre, oldTitle, newTitle):
    for i, movies in enumerate(movie_genres[genre]):
        if movies == oldTitle:
            movie_genres[genre][i] = newTitle


update_movies("Action", "Spiderman Brand new day", "Spiderman")

print(movie_genres)