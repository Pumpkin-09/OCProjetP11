from tests.conftest import clubs_fixture, competitions_fixture
from server import clubs, competitions


def test_showSummary_status_code_ok(client, mocker, clubs_fixture, competitions_fixture):

    mocker.patch("server.clubs", clubs_fixture)
    mocker.patch("server.competitions", competitions_fixture)

    response = client.post("/showSummary", data={"email": "exemple@exemple.com"})

    assert response.status_code == 200


def test_showSummary_status_code_redirect(client, mocker, clubs_fixture, competitions_fixture):

    mocker.patch("server.clubs", clubs_fixture)
    mocker.patch("server.competitions", competitions_fixture)

    response = client.post("/showSummary", data={"email": "error@exemple.com"})

    assert response.status_code == 302


def test_book_status_code_ok(client, mocker, clubs_fixture, competitions_fixture):

    mocker.patch("server.clubs", clubs_fixture)
    mocker.patch("server.competitions", competitions_fixture)

    response = client.get("/book/competitionName/clubName")

    assert response.status_code == 200


def test_book_status_code_redirect(client, mocker, clubs_fixture, competitions_fixture):

    mocker.patch("server.clubs", clubs_fixture)
    mocker.patch("server.competitions", competitions_fixture)

    response = client.get("/book/errorcompetitionName/errorclubName")

    assert response.status_code == 302


def test_purchasePlaces_status_code_ok(client, mocker, clubs_fixture, competitions_fixture):
    mocker.patch("server.clubs", clubs_fixture)
    mocker.patch("server.competitions", competitions_fixture)
    places_required = 3

    response = client.post(
        "/purchasePlaces",
        data={
            "club": clubs_fixture[0]["name"],
            "competition": competitions_fixture[0]["name"],
            "places": places_required
            }
        )

    assert response.status_code == 200
    assert int(clubs_fixture[0]["points"]) == 13 - places_required
    assert int(competitions_fixture[0]["numberOfPlaces"]) == 25 - places_required


def test_purchasePlaces_status_code_error_more_place(client, mocker, clubs_fixture, competitions_fixture):
    mocker.patch("server.clubs", clubs_fixture)
    mocker.patch("server.competitions", competitions_fixture)
    places_required = 20

    response = client.post(
        "/purchasePlaces",
        data={
            "club": clubs_fixture[0]["name"],
            "competition": competitions_fixture[0]["name"],
            "places": places_required
            }
        )

    assert response.status_code == 200
    assert "Maximum 12 places par club" in response.get_data(as_text=True)


def test_purchasePlaces_status_code_error_no_place(client, mocker, clubs_fixture, competitions_fixture_no_place):
    mocker.patch("server.clubs", clubs_fixture)
    mocker.patch("server.competitions", competitions_fixture_no_place)
    places_required = 3

    response = client.post(
        "/purchasePlaces",
        data={
            "club": clubs_fixture[0]["name"],
            "competition": competitions_fixture_no_place[0]["name"],
            "places": places_required
            }
        )

    assert response.status_code == 200
    assert "Pas assez de place disponible" in response.get_data(as_text=True)


def test_purchasePlaces_status_code_error_date_past(client, mocker, clubs_fixture, competitions_fixture_date_past):
    mocker.patch("server.clubs", clubs_fixture)
    mocker.patch("server.competitions", competitions_fixture_date_past)
    places_required = 3

    response = client.post(
        "/purchasePlaces",
        data={
            "club": clubs_fixture[0]["name"],
            "competition": competitions_fixture_date_past[0]["name"],
            "places": places_required
            }
        )

    assert response.status_code == 200
    assert "Cette compétition est terminée" in response.get_data(as_text=True)


def test_purchasePlaces_status_code_error_no_points(client, mocker, clubs_fixture_no_point, competitions_fixture):
    mocker.patch("server.clubs", clubs_fixture_no_point)
    mocker.patch("server.competitions", competitions_fixture)
    places_required = 3

    response = client.post(
        "/purchasePlaces",
        data={
            "club": clubs_fixture_no_point[0]["name"],
            "competition": competitions_fixture[0]["name"],
            "places": places_required
            }
        )

    assert response.status_code == 200
    assert "Points insufisant" in response.get_data(as_text=True)
