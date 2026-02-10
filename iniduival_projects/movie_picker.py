#IC 1st Movie Picker
import csv
from dataclasses import dataclass
from typing import List, Optiona

@dataclass
class Movie:
    title: str
    year: Optional[int]
    genres: List[str]
    director: Optional[str]
    actors: List[str]
    length: Optional[int]

def normalize_list(raw: str, separators: List[str]) -> List[str]:
    if not raw:
        return []
    parts = [raw]
    for sep in separators:
        new_parts = []
        for p in parts:
            new_parts.extend(p.split(sep))
        parts = new_parts
    return [p.strip().lower() for p in parts if p.strip()]


def parse_movies(csv_path: str) -> List[Movie]:
    movies = []
    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    title = (row.get("title") or "").strip()
                    if not title:
                        continue

                    year_raw = (row.get("year") or "").strip()
                    year = int(year_raw) if year_raw.isdigit() else None

                    genres = normalize_list((row.get("genres") or "").strip(), ["|"])
                    director_raw = (row.get("director") or "").strip()
                    director = director_raw.lower() if director_raw else None

                    actors = normalize_list((row.get("actors") or "").strip(), [";", ","])

                    length_raw = (row.get("length") or "").strip()
                    length = int(length_raw) if length_raw.isdigit() else None

                    movies.append(
                        Movie(
                            title=title,
                            year=year,
                            genres=genres,
                            director=director,
                            actors=actors,
                            length=length,
                        )
                    )
                except Exception:
                    continue
    except FileNotFoundError:
        print(f"Error: Could not find file '{csv_path}'.")
        return []

    return movies

def filter_by_genre(movies: List[Movie], query: str) -> List[Movie]:
    q = query.lower().strip()
    return [m for m in movies if m.genres and any(q in g for g in m.genres)]


def filter_by_director(movies: List[Movie], query: str) -> List[Movie]:
    q = query.lower().strip()
    return [m for m in movies if m.director and q in m.director]


def filter_by_actor(movies: List[Movie], query: str) -> List[Movie]:
    q = query.lower().strip()
    return [m for m in movies if m.actors and any(q in a for a in m.actors)]


def filter_by_length(movies: List[Movie], min_len: Optional[int], max_len: Optional[int]) -> List[Movie]:
    result = []
    for m in movies:
        if m.length is None:
            continue
        if min_len is not None and m.length < min_len:
            continue
        if max_len is not None and m.length > max_len:
            continue
        result.append(m)
    return result


def apply_filters(
    movies: List[Movie],
    genre: Optional[str],
    director: Optional[str],
    actor: Optional[str],
    min_len: Optional[int],
    max_len: Optional[int],
) -> List[Movie]:

    filtered = movies
    if genre:
        filtered = filter_by_genre(filtered, genre)
    if director:
        filtered = filter_by_director(filtered, director)
    if actor:
        filtered = filter_by_actor(filtered, actor)
    filtered = filter_by_length(filtered, min_len, max_len)
    return filtered

def format_movie(m: Movie) -> str:
    genres = " | ".join(g.title() for g in m.genres) if m.genres else "N/A"
    actors = ", ".join(a.title() for a in m.actors) if m.actors else "N/A"
    director = m.director.title() if m.director else "N/A"
    year = m.year if m.year is not None else "N/A"
    length = f"{m.length} min" if m.length is not None else "N/A"

    return (
        f'Title: "{m.title}" — Year: {year} — Genres: {genres} — '
        f"Director: {director} — Actors: {actors} — Length: {length}"
    )


def print_movie_list(movies: List[Movie]):
    if not movies:
        print("No movies to display.")
        return
    for i, m in enumerate(movies, start=1):
        print(f"{i}. {format_movie(m)}")


def print_intro():
    print("Welcome to the Movie Recommender!")
    print("Search by genre, director, actor, and length. Combine filters to refine results.\n")


def get_int_or_none(prompt: str) -> Optional[int]:
    raw = input(prompt).strip()
    if raw == "":
        return None
    if not raw.isdigit():
        print("Please enter a valid integer or leave blank.")
        return get_int_or_none(prompt)
    return int(raw)


def choose_filters() -> dict:
    print("\nChoose filters to apply (enter numbers separated by commas, e.g., 1,3):")
    print("1. Genre")
    print("2. Director")
    print("3. Actor")
    print("4. Length (min/max)")

    raw = input("Selected filters: ").strip()
    if not raw:
        print("No filters selected.")
        return {}

    try:
        choices = {int(x.strip()) for x in raw.split(",")}
    except ValueError:
        print("Invalid input. Try again.")
        return choose_filters()

    filters = {"genre": None, "director": None, "actor": None, "min": None, "max": None}

    if 1 in choices:
        filters["genre"] = input("Enter genre: ").strip()
    if 2 in choices:
        filters["director"] = input("Enter director: ").strip()
    if 3 in choices:
        filters["actor"] = input("Enter actor: ").strip()
    if 4 in choices:
        filters["min"] = get_int_or_none("Enter minimum length (or blank): ")
        filters["max"] = get_int_or_none("Enter maximum length (or blank): ")

    return filters

def search_flow(movies: List[Movie]):
    filters = choose_filters()

    results = apply_filters(
        movies,
        genre=filters.get("genre"),
        director=filters.get("director"),
        actor=filters.get("actor"),
        min_len=filters.get("min"),
        max_len=filters.get("max"),
    )

    if not results:
        print("\nNo movies match those filters. Try relaxing one.\n")
        return

    print("\nResults:\n")
    print_movie_list(results)

    while True:
        choice = input("\nEnter movie number for details, or press Enter to return: ").strip()
        if choice == "":
            break
        if not choice.isdigit():
            print("Invalid number.")
            continue
        idx = int(choice)
        if not (1 <= idx <= len(results)):
            print("Out of range.")
            continue
        print("\n" + format_movie(results[idx - 1]))

def main():
    MOVIES_FILE = "movies.csv"
    movies = parse_movies(MOVIES_FILE)

    if not movies:
        print("No movies loaded. Exiting.")
        return

    print_intro()

    while True:
        print("MAIN MENU:")
        print("1. Search / Get Recommendations")
        print("2. Print Full Movie List")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            search_flow(movies)
        elif choice == "2":
            print("\nFull Movie List:\n")
            print_movie_list(movies)
            print()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
