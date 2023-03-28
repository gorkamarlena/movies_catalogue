from unittest.mock import Mock
from tmdb_client import *
import pytest

from main import app


@pytest.mark.parametrize('list_type, result',(
        ('popular', 'movie/popular'),
        ('top_rated', 'movie/top_rated'),
        ('upcoming', 'movie/upcoming')
))
def test_homepage(monkeypatch,list_type, result):
    api_mock = Mock(return_value={"results": []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert get_single_movie(list_type) == call_tmdb_api(result)
    