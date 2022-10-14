import requests_with_caching
import json

# get_movies_from_tastedive: takes one input parameter as a string
# that is the name of a movie and returns the 5 TasteDive results
# that are similar to that movie


def get_movies_from_tastedive(movie_name):
    url = 'https://tastedive.com/api/similar'
    parameters = dict()
    parameters['limit'] = 5
    parameters['q'] = movie_name
    parameters['type'] = 'movies'
    response = requests_with_caching.get(url, params=parameters)
    response_json = response.json()
    return response_json

# extract_movie_titles: extracts the list of movie titles from the dictionary
# returned by get_movies_from_tastedive


def extract_movie_titles(json_str):
    movies_list = []
    for i in range(len(json_str['Similar']['Results'])):
        movie_name = json_str['Similar']['Results'][i]['Name']
        movies_list.append(movie_name)
    return movies_list

# get_related_titles: takes a list of movie titles as input and returns
# five related movies for each from TasteDive, extracts the titles for
# all of them, and combines them all into a single list


def get_related_titles(lst):
    related_titles_list = []
    for i in range(len(lst)):
        related_movies = extract_movie_titles(
            get_movies_from_tastedive(lst[i]))
        for i in range(len(related_movies)):
            returned_movie = related_movies[i]
            if returned_movie not in related_titles_list:
                related_titles_list.append(returned_movie)
    return related_titles_list


# get_movie_data: takes in one parameter as a string that represent the
# title of a movie and returns a dictionary with information about that movie

def get_movie_data(movie_title_str):
    _url = 'http://www.omdbapi.com/'
    parameters = dict()
    parameters['t'] = movie_title_str
    parameters['r'] = 'json'
    results = requests_with_caching.get(_url, params=parameters)
    results_json = results.json()
    return results_json

# get_movie_rating: takes a dictionary as an input which represents the
# information about a specific movie and returns its rating as an int


def get_movie_rating(d):
    rating = 0
    # d['Ratings'][1]['Source'] = Rotten Tomatoes
    # d['Ratings'][1]['Value'] = 83%
    for rate_dict in range(len(d['Ratings'])):
        if d['Ratings'][rate_dict]['Source'] == 'Rotten Tomatoes':
            rating_percentage = d['Ratings'][1]['Value']
            rating = int(rating_percentage[:-1])
    return rating

# get_sorted_recommendations takes a list of movie titles and returns a
# list of related titles sorted in descending order by their ratings on
# Rotten Tomatoes ratings


def get_sorted_recommendations(movie_titles):
    related_movies_dict = dict()
    sorted_related_movies = []
    temp = []
    related_movies = get_related_titles(movie_titles)
    # print(related_movies)
    for movie in related_movies:
        rating = get_movie_rating(get_movie_data(movie))
        related_movies_dict[movie] = rating
    # print(related_movies_dict)
    return [x[0] for x in sorted(related_movies_dict.items(), key=lambda item:(item[1], item[0]), reverse=True)]
    # return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]


# some invocations that we use in the automated tests;
# uncomment these if you are getting errors and want better error messages
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
