movies = [
    {
        "title": "Spider-Man: No Way Home",
        "genre": "Action",
        "year": 2021,
        "rating": 8.2,
        "description": "Peter Parker's identity is revealed, causing him \nto ask Doctor Strange for help. The spell goes wrong and brings villains \n from different universes.",
        "reviews": [
            {
                "user": "Kenneth",
                "rating": 9,
                "comment": "One of the best Spider-Man movies."
            },
            {
                "user": "Chris",
                "rating": 8,
                "comment": "Great action and a lot of emotional moments."
            },
        ]
    },

    {
        "title": "The Conjuring",
        "genre": "Horror",
        "year": 2013,
        "rating": 7.5,
        "description": "A family experiences terrifying supernatural events \nin their new home and seeks help from paranormal investigators.",
        "reviews": [
            {
                "user": "Robert",
                "rating": 8,
                "comment": "Very creepy and has a great atmosphere."
            },
            {
                "user": "Junelle",
                "rating": 7,
                "comment": "The story was interesting and scary."
            },
        ]
    },

    {
        "title": "Avengers: Endgame",
        "genre": "Action",
        "year": 2019,
        "rating": 8.4,
        "description": "The Avengers attempt to reverse the destruction caused \nby Thanos and bring back the people who disappeared.",
        "reviews": [
            {
                "user": "Kenneth",
                "rating": 9,
                "comment": "A great conclusion to a huge story."
            },
            {
                "user": "Robert",
                "rating": 8,
                "comment": "The final battle was amazing."
            },
        ]
    },

    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "year": 2014,
        "rating": 8.7,
        "description": "A group of astronauts travels through a wormhole in \nsearch of a new home for humanity as Earth becomes increasingly difficult to live on.",
        "reviews": [
            {
                "user": "Chris",
                "rating": 9,
                "comment": "Amazing visuals and story."
            },
            {
                "user": "Junelle",
                "rating": 9,
                "comment": "The science and emotional story worked really well together."
            },
        ]
    },

    {
        "title": "How to Train Your Dragon",
        "genre": "Fantasy",
        "year": 2010,
        "rating": 8.1,
        "description": "A young Viking named Hiccup becomes friends with a wounded \ndragon and begins to challenge the beliefs of his village.",
        "reviews": [
            {
                "user": "Junelle",
                "rating": 9,
                "comment": "A fun and emotional movie."
            },
            {
                "user": "Kenneth",
                "rating": 8,
                "comment": "Toothless is one of the best animated characters."
            },
        ]
    },

    {
        "title": "The Notebook",
        "genre": "Romance",
        "year": 2004,
        "rating": 7.8,
        "description": "A young couple from different social backgrounds falls in \nlove and struggles to stay together despite the challenges they face.",
        "reviews": [
            {
                "user": "Chris",
                "rating": 8,
                "comment": "A very emotional romance movie."
            },
        ]
    },

    {
        "title": "The Dark Knight",
        "genre": "Action",
        "year": 2008,
        "rating": 9.0,
        "description": "Batman faces the Joker, a criminal mastermind who creates \nchaos throughout Gotham City and challenges Batman's principles.",
        "reviews": [
            {
                "user": "Robert",
                "rating": 10,
                "comment": "One of the best superhero movies ever made."
            },
            {
                "user": "Kenneth",
                "rating": 9,
                "comment": "The Joker's character was incredible."
            },
        ]
    },

    {
        "title": "Inside Out",
        "genre": "Comedy",
        "year": 2015,
        "rating": 8.0,
        "description": "A young girl experiences major changes in her life while the \nemotions inside her mind try to help her adjust.",
        "reviews": [
            {
                "user": "Junelle",
                "rating": 8,
                "comment": "A creative and meaningful animated movie."
            },
        ]
    }
]

def getGenre():
    genres = []

    for movie in movies:
        if movie["genre"] not in genres:
            genres.append(movie["genre"])
    
    return genres