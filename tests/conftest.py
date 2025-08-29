import pytest
from datetime import datetime, timedelta
from server import app


@pytest.fixture(scope='session')
def client():
    # Ici, nous configurons le client de test
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client


@pytest.fixture
def clubs_fixture():
    data = [{
        "name":"clubName",
        "email":"exemple@exemple.com",
        "points":"13"
    }]

    return data


@pytest.fixture
def clubs_fixture_no_point():
    data = [{
        "name":"clubName",
        "email":"exemple@exemple.com",
        "points":"1"
    }]

    return data


@pytest.fixture
def competitions_fixture():
    data = [{
            "name": "competitionName",
            "date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "numberOfPlaces": "25"
        }]

    return data

@pytest.fixture
def competitions_fixture_no_place():
    data = [{
            "name": "competitionName",
            "date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "numberOfPlaces": "1"
        }]

    return data


@pytest.fixture
def competitions_fixture_date_past():
    data = [{
            "name": "competitionName",
            "date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "numberOfPlaces": "25"
        }]

    return data
