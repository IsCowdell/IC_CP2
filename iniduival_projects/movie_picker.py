#IC 1st Movie Picker
import csv

def load_movies(filename):
    movies = []

    try:
        with open(filename, newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                movie = {
                    "title": row["title"],
                    "year": row["year"],
                    "genre": row["genres"].lower(),
                    "director": row["director"].lower(),
                    "actors": row["actors"].lower(),
                    "length": row["length"]
                }

                movies.append(movie)

    except FileNotFoundError:
        print("File not found.")
        return []

    return movies


def search_movies(movies):
    print("\nSearch for a movie!")
    genre = input("Enter a genre (or press Enter to skip): ").lower()
    director = input("Enter a director (or press Enter to skip): ").lower()
    actor = input("Enter an actor (or press Enter to skip): ").lower()

    results = []

    for movie in movies:
        if genre and genre not in movie["genre"]:
            continue
        if director and director not in movie["director"]:
            continue
        if actor and actor not in movie["actors"]:
            continue

        results.append(movie)

    if not results:
        print("\nNo movies found.")
        return

    print("\nMovies Found:\n")
    for i in range(len(results)):
        m = results[i]
        print(f"{i+1}. {m['title']} ({m['year']})")


def main():
    movies = load_movies("movies.csv")

    if not movies:
        return

    print("Welcome to the Movie Picker!")

    while True:
        print("\n1. Search for a movie")
        print("2. Show all movies")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            search_movies(movies)

        elif choice == "2":
            for movie in movies:
                print(movie["title"], "(", movie["year"], ")")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()
