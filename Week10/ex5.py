class Movie:
    def __init__(self, titel, director, score):
        self.titel = titel
        self.director = director
        self.score = score

movie1 = Movie("Titel1", "Director1", 11)
movie2 = Movie("Titel2", "Director1", 22)
movie3 = Movie("Titel3", "Director3", 33)

# List of all movies
movies = [movie1, movie2, movie3]

# Ask the user for the director's name
director_name = input("Enter the director's name: ")

# Find the movies directed by the given director
director_movies = [movie for movie in movies if movie.director == director_name]

# If the director has any movies, find the one with the highest score
if director_movies:
    highest_rated_movie = max(director_movies, key=lambda movie: movie.score)
    print(f"The highest scoring movie from {director_name} is '{highest_rated_movie.titel}' with a score of {highest_rated_movie.score}.")
else:
    print(f"No movies found for director {director_name}.")



