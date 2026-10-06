SELECT t.id, c.name, d.full_name AS driver, t.status,
       t.created, t.from_addr, t.to_addr
FROM trips t
LEFT JOIN clients c ON c.id = t.client_id
LEFT JOIN drivers d ON d.id = t.driver_id
WHERE t.status IN ('cancelled','no_show')
ORDER BY t.created DESC;
