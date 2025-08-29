from server import loadClubs, loadCompetitions


def test_loadClubs():
    data = loadClubs()

    assert len(data) > 0
    assert isinstance(data, list)


def test_loadCompetitions():
    data = loadCompetitions()

    assert len(data) > 0
    assert isinstance(data, list)


def test_integration_showSummary_status_code_ok(client):
    response = client.post("/showSummary", data={'email': "john@simplylift.co"})
    assert response.status_code == 200


def test_integration_showSummary_status_code_redirect(client):
    response = client.post("/showSummary", data={'email': "error@exemple.com"})
    assert response.status_code == 302


def test_book_status_code_ok(client):
    response = client.get("/book/Spring Festival/Simply Lift")
    assert response.status_code == 200
