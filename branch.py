Movies = [ {"Movie Name" : "Spiderman", "Genre" : "Fiction"},
{"Movie Name" : "Cars", "Genre" : "Fantasy"},
{"Movie Name" : "dasd", "Genre" : "Horror"}
]

def add_movie(movies):
    add = input ("Enter Movie Name: ")
    add_genre = input ("Enter Movie Genre: ")
    
    
    movie_exists = any(m["Movie Name"] == add for m in movies)
    
    if movie_exists:
        print("Movie already exists!")
    else:
        movies.append({"Movie Name": add, "Genre": add_genre})
        print("Movie added!")
        print(movies)


add_movie(Movies)