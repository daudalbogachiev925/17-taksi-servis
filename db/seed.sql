INSERT INTO tariffs (name, base, per_km, per_min, min_fare) VALUES
('Эконом',100,15,3,150),
('Комфорт',200,25,5,250),
('Бизнес',500,50,10,600);

INSERT INTO drivers (full_name, phone, car, plate, rating) VALUES
('Иван Петров','+7900','Kia Rio','А123БВ',4.8),
('Сергей Иванов','+7901','Toyota Camry','Г456ДЕ',4.9),
('Дмитрий Попов','+7902','Mercedes E','Ж789ЗИ',5.0);

INSERT INTO clients (name, phone) VALUES
('Аня','+7910'),('Петя','+7911'),('Катя','+7912');

INSERT INTO trips (driver_id, client_id, tariff_id, from_addr, to_addr,
                   distance_km, duration_min, price, commission, status) VALUES
(1,1,1,'ул. Ленина 5','ул. Мира 10',5.2,15,220,44,'done'),
(2,2,2,'пр. Мира 10','ул. Пушкина 15',8.5,25,450,90,'done'),
(1,3,1,'ул. Садовая 20','ул. Тверская 5',3.0,10,150,30,'done'),
(3,1,3,'ул. Ленина 5','аэропорт',35.0,50,2000,400,'in_progress');
