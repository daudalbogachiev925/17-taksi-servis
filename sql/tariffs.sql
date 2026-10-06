SELECT tar.name,
       COUNT(t.id) AS trips,
       SUM(t.price) AS revenue,
       ROUND(AVG(t.price),2) AS avg_price,
       ROUND(AVG(t.distance_km),2) AS avg_km
FROM tariffs tar
LEFT JOIN trips t ON t.tariff_id = tar.id AND t.status='done'
GROUP BY tar.id
ORDER BY revenue DESC;
