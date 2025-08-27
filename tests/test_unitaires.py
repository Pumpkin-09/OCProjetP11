from Python_Testing.tests.conftest import clubs_fixture, competitions_fixture
from Python_Testing import server


def test_showSummary_status_code_ok(client, mocker, clubs_fixture, competitions_fixture):

    mocker.patch.object(server.clubs, clubs_fixture)
    mocker.patch.object(server.competitions, competitions_fixture)

    response = client.post('/showSummary', data={'email': 'exemple@exemple.com'})

    assert response.status_code == 200


def test_showSummary_status_code_redirect(client, mocker, clubs_fixture, competitions_fixture):

    mocker.patch.object(server.clubs, clubs_fixture)
    mocker.patch.object(server.competitions, competitions_fixture)

    response = client.post('/showSummary', data={'email': 'error@exemple.com'})

    assert response.status_code == 302
