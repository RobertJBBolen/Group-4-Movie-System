movie_genres = {
    "Action": ["Spiderman Brand new day"],
    "Musical": ["Mamma Mia"],
    "Comedy": ["Mean Girls"],
    "Sci-Fi": ["Star wars"]
}

def add_movie():
    title = input("Enter Movie Name: ")
    genre = input("Enter Movie Genre: ")

    if genre not in movie_genres:
        movie_genres[genre] = []

    if title in movie_genres[genre]:
        print("Movie already exists!")

    else:
        movie_genres[genre].append(title)
        print(f"'{title}' has been added!")

add_movie()
