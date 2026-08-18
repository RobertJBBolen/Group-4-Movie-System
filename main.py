#MAIN (user login, UI and such here)

# Features

# CREATE / (Add Movies (Genre, Title))

# READ / (Search movies(Genre -> Movie), Show Reviews and comments etc.)

# UPDATE / (Updating Movie titles & managing movies.)

# DELETE / (Delete movies)

from movie import movies

def search():
    while True:
        try:
            print("\nSEARCH MOVIES\n")

            keyword = input("Enter movie title or genre: ").strip().lower()
            found = False

            for movie in movies:
                try:
                    if keyword in movie["title"].lower() or keyword in movie["genre"].lower():
                        print(f"\nTitle: {movie['title']}")
                        print(f"Genre: {movie['genre']}")
                        print(f"Year: {movie['year']}")
                        print(f"Rating: {movie['rating']}/10")
                        print(f"Description: {movie['description']}")
                        if "reviews" in movie and movie["reviews"]:
                            print("Reviews:")
                            for review in movie["reviews"]:
                                print(f"  - {review['user']} ({review['rating']}/10): {review['comment']}")
                        else:
                            print("Reviews: No reviews yet.")
                        print("-" * 60)
                        found = True
                except KeyError as e:
                    print(f"Warning: Missing field {e} in movie data")
                    continue

            if not found:
                print("\nNo movies found.")
                search_again = input("Do you want to search again? (yes/no): ").strip().lower()
                if search_again not in ['yes', 'y']:
                    return  # Exit the function and return to main menu
            else:
                search_again = input("\nDo you want to search again? (yes/no): ").strip().lower()
                if search_again not in ['yes', 'y']:
                    return  # Exit the function and return to main menu
        except Exception as e:
            print(f"\nAn error occurred during search: {e}")
            input("\nPress Enter to try again...")
            continue

def view_and_review():
    try:
        print("\n--- VIEW & REVIEW MOVIES ---")
        
        count = 1
        movie_list = []
        
        for movie in movies:
            print(f"{count}. {movie['title']} ({movie['genre']})")
            movie_list.append(movie)
            count += 1
                
        
        try:
            choice = int(input("\nEnter movie number: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            input("\nPress Enter to return...")
            return
        
        if choice >= 0 and choice < len(movie_list):
            selected_movie = movie_list[choice]
            print(f"\n--- Details for: {selected_movie['title']} ---")
            print(f"Genre: {selected_movie['genre']}")
            print(f"Year: {selected_movie['year']}")
            print(f"Rating: {selected_movie['rating']}")
            print(f"Description: {selected_movie['description']}")
            
            # Show reviews if any exist
            if "reviews" in selected_movie and selected_movie["reviews"]:
                print("\nReviews:")
                for review in selected_movie["reviews"]:
                    print(f"  - {review['user']} ({review['rating']}/10): {review['comment']}")
            else:
                print("\nNo reviews yet.")
        else:
            print("Invalid number choice.")
            
        input("\nPress Enter to return...")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        input("\nPress Enter to return...")

# Call main function
if __name__ == "__main__":
    search()