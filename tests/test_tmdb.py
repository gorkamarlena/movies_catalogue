import tmdb_client
from unittest.mock import Mock
import pytest

def test_get_single_movie(monkeypatch):
   result = {'title': 'movie'}

   get_tmdb_response_mock = Mock()
   get_tmdb_response_mock.return_value = result
   monkeypatch.setattr('tmdb_client.get_tmdb_response', get_tmdb_response_mock)

   assert tmdb_client.get_single_movie(0) == result

def test_get_single_movie_cast_endpoint(monkeypatch):
   result = "https://api.themoviedb.org/3/movie/12/credits"

   get_tmdb_response_mock = Mock()
   get_tmdb_response_mock.return_value = {'cast': []}
   monkeypatch.setattr('tmdb_client.get_tmdb_response', get_tmdb_response_mock)

   tmdb_client.get_single_movie_cast(12)
   assert result in get_tmdb_response_mock.call_args.args

def test_get_movie_images(monkeypatch):
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   poster_url = tmdb_client.get_poster_url(poster_api_path, size="w342")
   assert expected_default_size in poster_url




