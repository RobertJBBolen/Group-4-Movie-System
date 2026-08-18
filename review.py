from movies import movies

def add_review():
    title = input("Enter movie title to review: ")
    
    movie_exists = False
    target_movie = None

    for m in movies:
        if m["title"] == title:
            movie_exists = True
            target_movie = m
            break

    if not movie_exists:
        print(f"Error: '{title}' is not in the movie library.")
        return
        
    user_name = input("Enter your name: ")

    try:
        rating = int(input("Enter rating (1-5 stars): "))
    except ValueError:
        print("Error: Rating must be a number.")
        return

    if rating < 1 or rating > 5:
        print("Error: Rating must be between 1 and 5 stars.")
        return

    comment = input("Enter your comment: ")

    target_movie["reviews"].append(
        {"user": user_name, "rating": rating, "comment": comment}
    )
    print(f"Review added for {title}!")

def show_reviews():
    title = input(
        "Enter movie title to view (or press Enter to view all): "
    ).strip()

    print("=" * 50)
    if title:
        movie_exists = False
        target_movie = None

        for m in movies:
            if m["title"] == title:
                movie_exists = True
                target_movie = m
                break

        if not movie_exists:
            print(f"Error: '{title}' is not in the movie library.")
            print("=" * 50)
            return

        reviews = target_movie["reviews"]
        if reviews:
            print(f"Reviews for '{title}':")
            for r in reviews:
                print(
                    f"  - [{r['user']}] Rating: {'★' * r['rating']} ({r['rating']}/5) | {r['comment']}"
                )
        else:
            print(f"No reviews found for '{title}'.")
    else:
        for m in movies:
            print(f"Movie: {m['title']}")
            for r in m["reviews"]:
                print(
                    f"  - [{r['user']}] Rating: {'★' * r['rating']} ({r['rating']}/5) | {r['comment']}"
                )
    print("=" * 50)
