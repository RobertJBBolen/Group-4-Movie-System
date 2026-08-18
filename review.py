movie_genres = {
    "Action": ["Spiderman Brand new day"],
    "Musical": ["Mamma Mia"],
    "Comedy": ["Mean Girls"],
    "Sci-Fi": ["Star wars"]
}
movie_reviews = {}

def add_review():
    title = input("Enter movie title to review: ")

    if title:
        movie_exists = False
        for movies in movie_genres.values():
            if title in movies:
                movie_exists = True
                break

    if not movie_exists:
        print(f"Error: '{title}' is not in the movie library.")
        return
    try:
        rating = int(input("Enter rating (1-5 stars): "))
    except ValueError:
        print("Error: Rating must be a number.")
        return

    if rating < 1 or rating > 5:
        print("Error: Rating must be between 1 and 5 stars")
        return

    comment = input("Enter your comment: ")

    if title not in movie_reviews:
        movie_reviews[title] = []

    movie_reviews[title].append({"rating": rating, "comment": comment})
    print(f"Review added for {title}!")

def show_reviews():
    title = input("Enter movie title to view (or press Enter to view all): ").strip()

    if title:
        movie_exists = False
        for movies in movie_genres.values():
            if title in movies:
                movie_exists = True
                break

        if not movie_exists:
            print(f"Error: '{title}' is not in the movie library.")
            print("=" * 50)
            return

        reviews = movie_reviews.get(title, [])
        if reviews:
            print(f"Reviews for '{title}':")
            for r in reviews:
                print(f"  - Rating: {'★' * r['rating']} ({r['rating']}/5) | {r['comment']}")
        else:
            print(f"No reviews found for '{title}'.")

# pang test lang puu
add_review()
add_review()

show_reviews()
