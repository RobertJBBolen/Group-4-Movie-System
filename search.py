import Branch;
def search_movie(movie_name):

def search_and_get_movie(movie_name):
    ia = Branch()
    
    results = ia.search_movie(movie_name)
    
    if not results:
        print("No movies found.")
        return

   
    print(f"Found {len(results)} results for '{movie_name}':")
    for index, movie in enumerate(results[:5]): # Show top 5
        print(f"{index + 1}. {movie['title']} ({movie.get('year', 'Unknown Year')})")
        
   t
    first_movie = results[0]
    movie_id = first_movie.movieID
    details = ia.get_movie(movie_id)
    
    print("\n--- Movie Details ---")
    print(f"Title: {details.get('title')}")
    print(f"Year: {details.get('year')}")
    print(f"Rating: {details.get('rating')}")
    print(f"Genres: {', '.join(details.get('genres', ['N/A']))}")
    print(f"Plot: {details.get('plot', ['N/A'])[0].split('::')[0]}")
