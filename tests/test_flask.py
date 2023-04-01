from unittest.mock import Mock
from tmdb_client import *
import pytest


from main import app


@pytest.mark.parametrize("list_type",
                         [
                             'popular',
                             'top_rated',
                             'now_playing',
                             'upcoming'
                         ]
                         )

def test_homepage(monkeypatch, list_type):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr('tmdb_client.get_tmdb_response', api_mock)

    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
        assert response.status_code == 200
        api_mock.assert_called_once_with(f'https://api.themoviedb.org/3/movie/{list_type}')
    