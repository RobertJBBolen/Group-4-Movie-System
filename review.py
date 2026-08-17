movie_genres = {"Action": ["Spiderman Brand new day"],
            "Musical": ["Mamma Mia"],
            "Comedy": ["Mean Girls"],
            "Sci-Fi": ["Star wars"]
}
movie_reviews = {}

def add_review(title, rating, comment):
    if rating < 1 or rating > 5:
        print("Error: Rating must be between 1 and 5 stars")
        return

    if title not in movie_reviews:
        movie_reviews[title] = []

    movie_reviews[title].append({"rating": rating, "comment": comment})
    print(f"Review added for {title}!")

def show_reviews(title=None):

    print("=" * 50)
    if title:
        reviews = movie_reviews.get(title, [])
        print(f"Reviews for '{title}':")
        
        for r in reviews:
            print(f"  - Rating: {'★' * r['rating']} ({r['rating']}/5) | {r['comment']}")
    else:
        for title, reviews in movie_reviews.items():
            print(f"Movie: {title}")
        for r in reviews:
            print(f"  - Rating: {'★' * r['rating']} ({r['rating']}/5) | {r['comment']}")
    print("=" * 50)


add_review("Spiderman", 5, "Great action sequences!")
add_review("Spiderman", 4, "Enjoyed the storyline.")
add_review("Mean Girls", 5, "Classic comedy.")


show_reviews()

show_reviews("Spiderman")