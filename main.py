#MAIN (user login, UI and such here)

# Features

# CREATE / (Add Movies (Genre, Title))

# READ / (Search movies(Genre -> Movie), Show Reviews and comments etc.)

# UPDATE / (Updating Movie titles & managing movies.)

# DELETE / (Delete movies)

movie_genres = {
    "Action": ["Spiderman Brand new day"],
    "Musical": ["Mamma Mia"],
    "Comedy": ["Mean Girls"],
    "Sci-Fi": ["Star wars"]
}

def search():
    print("\nSEARCH MOVIES\n")

    keyword = input("Enter movie title or genre: ").strip().lower()
    found = False

    for genre, titles in movie_genres.items():
        for title in titles:
            if keyword in title.lower() or keyword in genre.lower():
                print(f"\nTitle: {title}")
                print(f"Genre: {genre}")
                found = True

    if not found:
        print("\nNo movies found.")

    input("\nPress Enter to return to main menu...")

def view_and_review():
    print("\n--- VIEW & REVIEW MOVIES ---")
    
    
    count = 1
    movie_list = []
    
    for genre in movie_genres:
        for movie in movie_genres[genre]:
            print(f"{count}. {movie}")
            movie_list.append(movie)
            count += 1
            
    
    choice = int(input("\nEnter movie number: ")) - 1
    
    if choice >= 0 and choice < len(movie_list):
        selected_movie = movie_list[choice]
        print(f"\n--- Details for: {selected_movie} ---")
        
        # Show reviews if any exist
        if selected_movie in reviews:
            print("Reviews:", reviews[selected_movie])
        else:
            print("No reviews yet.")
            
        # Add a review option
        new_review = input("Write a review (press Enter to skip): ")
        if new_review != "":
            if selected_movie not in reviews:
                reviews[selected_movie] = []
            reviews[selected_movie].append(new_review)
            print("Review saved!")
    else:
        print("Invalid number choice.")
        
    input("\nPress Enter to return...")

# Call main function
if __name__ == "__main__":
    search()