def test_dev_test(client, db):
    r = client.get('/')
    assert r.status_code == 200

def test_dev_404(client, db):
    r = client.get('/')
    assert r.status_code == 404
