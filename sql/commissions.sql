SELECT t.id,
       c.name AS client, d.full_name AS driver, tar.name AS tariff,
       t.price, t.commission,
       ROUND(100.0 * t.commission / t.price, 1) AS commission_pct
FROM trips t
JOIN clients c ON c.id = t.client_id
JOIN drivers d ON d.id = t.driver_id
JOIN tariffs tar ON tar.id = t.tariff_id
WHERE t.status='done'
ORDER BY t.created DESC
LIMIT 50;
