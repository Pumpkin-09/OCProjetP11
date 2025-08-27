import pytest


@pytest.fixture
def clubs_fixture():
    data = [{
        "name":"club name",
        "email":"exemple@exemple.com",
        "points":"13"
    }]

    return data


@pytest.fixture
def competitions_fixture():
    data = [{
            "name": "competition name",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        }]

    return data
