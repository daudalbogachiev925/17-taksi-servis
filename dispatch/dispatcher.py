import math

def distance(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def dispatch(client_pos, drivers, max_km=5):
    """Находит ближайших водителей в радиусе max_km."""
    available = []
    for d in drivers:
        if not d['available']:
            continue
        dist = distance(client_pos, (d['lat'], d['lon']))
        if dist <= max_km:
            available.append({**d, 'distance': dist})
    return sorted(available, key=lambda x: x['distance'])
