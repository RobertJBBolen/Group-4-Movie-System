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

def update_movies():
    genre = input("Enter genre to update: ")
    
    if genre in movie_genres:
        oldTitle = input("Enter old title: ")
        
        if oldTitle in movie_genres[genre]:
            newTitle = input("Enter new title: ")
            
            for i, movies in enumerate(movie_genres[genre]):
                if movies == oldTitle:
                    movie_genres[genre][i] = newTitle
            print(f"Successfully updated '{oldTitle}' to '{newTitle}'.")
        else:
            print(f"Error: Could not find '{oldTitle}' in '{genre}'.")
    else:
        print(f"Error: Genre '{genre}' does not exist.")

def delete_movies():
    genre = input("Enter genre to delete from: ")
    
    if genre in movie_genres:
        title = input("Enter movie title to delete: ")
        
        if title in movie_genres[genre]:
            movie_genres[genre].remove(title)
            print(f"Successfully deleted '{title}'.")
        else:
            print(f"Error: Could not find '{title}' in '{genre}'.")
    else:
        print(f"Error: Genre '{genre}' does not exist.")

# pang test lang to sa mga functions
update_movies()
show_Movies()

delete_movies()
show_Movies()
