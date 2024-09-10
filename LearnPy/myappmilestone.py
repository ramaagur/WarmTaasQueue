"""
Enter 'a' to add a movie, 'l' to see the movies, 'f' to find the movies and 'q' to quit the movies

--Add Movies
--show movies
--find a movie
-stop running the movie

Tasks:
[]: Decide where to store the movie
[]: what is the format of the movie
[]: show user the main interface and get their input
[]: Allow users to add movie
[]: show all their movies
[]: Find a  movie
[]: Stop running the program when they enter 'q'
"""
movies = []
"""
     movie = {
     'name':         (str),
     'director':     (str),
     'year':         (int)
     }   
"""


def menu():
    user_input = input ( "Enter 'a', 'l' , 'f' and 'q'  :  " )

    while user_input != 'q':
        if user_input == 'a':
            add_movie ()
        elif user_input == 'l':
            show_movie(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print ( "unknown command" )

        user_input = input ( "Enter 'a', 'l' , 'f' and 'q'  :  " )


def add_movie():
    name = input ( "Enter a movie name  :  " )
    director = input ( "Enter a directr name  :  " )
    year = int ( input ( "Enter a movie name  :  " ) )

    movies.append ( {
        'name': name,
        'director': director,
        'year': year
    } )

    ##FUNCTIONS SHOW MOVIES IN MOVIE

def show_movie(movies_list):
    for movie in movies_list:
        show_movie_details(movies)

def show_movie_details(movies):
    print(f"name:{movies['name']}")
    print(f"director:{movies['director']}")
    print(f"year:{movies['year']}")
def find_movie():
    find_by = input("enter what movie category you are finding :")
    looking_for = input("What part of the are you looking for : ")
    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])
    show_movies(found_movies)

def find_by_attribute(items, expected, finder):
     found = []
     for i in items:
         if finder(i) == expected:
           found.append(i)