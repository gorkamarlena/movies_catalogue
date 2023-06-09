import requests, random

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

def get_tmdb_response(url: str) -> dict:
    headers = {'Authorization': f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_list(list_name: str = 'popular', list_len: int = 12) -> list:
    url = f"https://api.themoviedb.org/3/movie/{list_name}"
    result = get_tmdb_response(url)
    try:
        rand_movie_list = random.sample(result.get('results'), k=list_len)
        return rand_movie_list
    except ValueError:
        return result.get('results')[:list_len]

def get_single_movie(movie_id: int) -> dict:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    result = get_tmdb_response(url)
    return result

def get_single_movie_cast(movie_id: int, list_len: int = 4) -> list:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    result = get_tmdb_response(url)
    return result.get('cast', [])[:list_len]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()
    


