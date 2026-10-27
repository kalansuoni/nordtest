import requests


def test_status_code():
    """Make sure the API call succeeds."""
    url = 'https://api.github.com/search/repositories'
    url += '?q=language:python+sort:stars+stars:>10000'

    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200


def test_repository_count():
    """Make sure repositories are returned."""
    url = 'https://api.github.com/search/repositories'
    url += '?q=language:python+sort:stars+stars:>10000'

    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)

    response_dict = response.json()

    assert len(response_dict['items']) > 0


def test_total_count():
    """Check that GitHub reports many matching repos."""
    url = 'https://api.github.com/search/repositories'
    url += '?q=language:python+sort:stars+stars:>10000'

    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)

    response_dict = response.json()

    assert response_dict['total_count'] > 100


def test_default_items_returned():
    """GitHub should return up to 30 items by default."""
    url = 'https://api.github.com/search/repositories'
    url += '?q=language:python+sort:stars+stars:>10000'

    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)

    response_dict = response.json()

    assert len(response_dict['items']) <= 30