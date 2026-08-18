from movie import movies
width = 60

def search():
    while True:
        try:
            print()
            print("="*width)
            print("\n"+"SEARCH MOVIES".center(width)+"\n")
            print("="*width)

            keyword = input("\nEnter movie title or genre: ").strip().lower()

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
                        print("-" * width)
                        found = True
                except KeyError as e:
                    print(f"Warning: Missing field {e} in movie data")
                    continue

            if not found:
                print("\nNo movies found.")
                search_again = input("\nDo you want to search again? (yes/no): ").strip().lower()
                if search_again not in ['yes', 'y']:
                    return  # Exit the function and return to main menu
                # If yes, loop continues and prompts for another search
            else:
                input("\nPress Enter to continue searching or type to search again...")
                search_again = input("Do you want to search again? (yes/no): ").strip().lower()
                if search_again not in ['yes', 'y']:
                    return  # Exit the function and return to main menu
        except Exception as e:
            print(f"\nAn error occurred during search: {e}")
            print("Please try again.")
            input("\nPress Enter to continue...")
            