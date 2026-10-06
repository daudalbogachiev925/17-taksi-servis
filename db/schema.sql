CREATE TABLE tariffs (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    base NUMERIC(10,2) NOT NULL,
    per_km NUMERIC(10,2) NOT NULL,
    per_min NUMERIC(10,2) NOT NULL,
    min_fare NUMERIC(10,2) DEFAULT 0
);

CREATE TABLE drivers (
    id BIGSERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    phone TEXT,
    car TEXT,
    plate TEXT UNIQUE,
    rating NUMERIC(3,2) DEFAULT 5.0,
    lat NUMERIC(9,6),
    lon NUMERIC(9,6),
    available BOOLEAN DEFAULT TRUE,
    status TEXT DEFAULT 'active'
);

CREATE TABLE clients (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT,
    rating NUMERIC(3,2) DEFAULT 5.0
);

CREATE TABLE trips (
    id BIGSERIAL PRIMARY KEY,
    driver_id BIGINT REFERENCES drivers(id),
    client_id BIGINT REFERENCES clients(id),
    tariff_id INT REFERENCES tariffs(id),
    from_addr TEXT,
    to_addr TEXT,
    distance_km NUMERIC(6,2),
    duration_min INT,
    price NUMERIC(10,2),
    commission NUMERIC(10,2),
    status TEXT DEFAULT 'requested',
    created TIMESTAMP DEFAULT NOW(),
    finished TIMESTAMP
);

CREATE INDEX idx_trips_driver ON trips(driver_id);
CREATE INDEX idx_trips_status ON trips(status);
CREATE INDEX idx_trips_created ON trips(created);
