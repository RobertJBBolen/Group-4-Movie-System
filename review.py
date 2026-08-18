from movie import movies
from editmovies import *

def addReview():
    show_Movies()
    title = input("Enter movie title to review: ")

    target_movie = None
    for m in movies:
        if m["title"] == title:
            target_movie = m
            break

    if not target_movie:
        print(f"Error: '{title}' is not in the movie library.")
        return

    user_name = input("Enter your name: ")

    try:
        rating = int(input("Enter rating (1-10 stars): "))
    except ValueError:
        print("Error: Rating must be a number.")
        return

    if rating < 1 or rating > 10:
        print("Error: Rating must be between 1 and 10 stars.")
        return

    comment = input("Enter your comment: ")

    target_movie["reviews"].append(
        {"user": user_name, "rating": rating, "comment": comment}
    )
    total_stars = sum(r["rating"] for r in target_movie["reviews"])
    num_reviews = len(target_movie["reviews"])
    target_movie["rating"] = round(total_stars / num_reviews, 1)

    print(f"Review added for '{title}'!")
    print(f"Updated average rating: {target_movie['rating']}/5")