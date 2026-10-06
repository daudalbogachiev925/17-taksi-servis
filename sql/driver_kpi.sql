SELECT d.id, d.full_name, d.car, d.rating,
       COUNT(t.id) AS trips,
       COUNT(t.id) FILTER (WHERE t.status='done') AS completed,
       SUM(t.distance_km) FILTER (WHERE t.status='done') AS km,
       SUM(t.price) FILTER (WHERE t.status='done') AS revenue
FROM drivers d
LEFT JOIN trips t ON t.driver_id = d.id
GROUP BY d.id
ORDER BY revenue DESC NULLS LAST;
