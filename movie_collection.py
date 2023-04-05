"""
Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

-Add Movies
-See Movies
-Find a Movie
-Stop running the program

Tasks:
[x]: Decide where to store movies
[x]: What is the format of a movie?
[x]: Show the user the main interface and get their input
[x]: Allow user tyo add movies
[x]: Show all their movies
[X]: Find a movie (by attribute)
[x]: Stop running the program when user types 'q'
"""
movies = []

"""
movie = (
    'name':(str),
    'director':(str),
    'year':(str),
}
"""


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        elif user_input == 'q':
            print('Goodbye!')
        else:
            print('Invalid option-please try again.')

        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")


def add_movie():
    title = input('Enter the movie title: ')
    director = input('Enter the movie director: ')
    year = input('Enter the movie release year: ')

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")


def find_movie():
    find_by = input("What property of the movie are you looking for? ")
    looking_for = input("What are you searching for? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


menu()






