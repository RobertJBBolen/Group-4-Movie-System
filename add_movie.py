from movie import movies, getGenre
width = 60 

def addMovie():
    print()
    print("="*width)
    print("\n"+"Add Movie".center(width)+"\n")
    print("="*width)
    try:
        title = input("\nEnter Movie Name: ").strip()

        if title == "":
            print("\nMovie name cannot be empty.")
            return

        genres = getGenre()

        print("\nGenres:")
        for i, genre in enumerate(genres, 1):
            print(f"[{i}] {genre}")

        while True:
            try:
                genre_choice = int(input("\nEnter Movie Genre: "))

                if 1 <= genre_choice <= len(genres):
                    genre = genres[genre_choice - 1]
                    break
                else:
                    print(f"Please enter a number from 1 to {len(genres)}.")

            except ValueError:
                print("\nInvalid input. Please enter numbers only.")

        while True:
            try:
                year = int(input("\nEnter Movie Year: "))

                if 1888 <= year <= 2100:
                    break
                else:
                    print("\nPlease enter a valid year.")

            except ValueError:
                print("\nInvalid input. Please enter numbers only.")

        description = input("Enter Movie Description: ").strip()

        if description == "":
            print("Movie description cannot be empty.")
            return

        for movie in movies:
            if movie["title"].lower() == title.lower():
                print("Movie already exists!")
                return

        movies.append({
            "title": title,
            "genre": genre,
            "year": year,
            "rating": 0,
            "description": description,
            "reviews": []
        })

        print(f"\n'{title}' has been added successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
