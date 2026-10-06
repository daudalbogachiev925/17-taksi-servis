from dispatch.dispatcher import dispatch

def test_dispatch_sorts_by_distance():
    client = (0, 0)
    drivers = [
        {'id':1, 'lat': 3, 'lon': 3, 'available': True},
        {'id':2, 'lat': 1, 'lon': 1, 'available': True},
        {'id':3, 'lat': 10, 'lon': 10, 'available': True},
    ]
    r = dispatch(client, drivers, max_km=20)
    assert r[0]['id'] == 2
    assert r[-1]['id'] == 3
