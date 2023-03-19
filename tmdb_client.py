import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZTU4MmNjYzQ0MmI5YzIwYzg0YjIyY2E2MTM5YTM1NSIsInN1YiI6IjY0MTE3OWNkYTZjMTA0MDBjMGM2MDEwYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9-luKdddIfnw834po92m0pK8rL4VhCrJ0voqFMjy4v0"

def get_popular_movies(list_type):
    categories_list = ['now_playing', 'top_rated', 'upcoming', 'popular']
    if list_type in categories_list:
        response = requests.get(f'https://api.themoviedb.org/3/movie/{list_type}?api_key=3d3db789bcf0716515f744cf39623dc2')
    else:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/popular?api_key=3d3db789bcf0716515f744cf39623dc2')
    response.raise_for_status()
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(list_type, how_many):
    data = get_popular_movies(list_type)
    return data["results"][:how_many]

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


