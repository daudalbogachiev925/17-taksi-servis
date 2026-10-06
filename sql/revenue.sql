SELECT date_trunc('day', created) AS day,
       COUNT(*) AS trips,
       SUM(price) AS gross,
       SUM(commission) AS commission,
       SUM(price) - SUM(commission) AS drivers_payout
FROM trips
WHERE status='done' AND created >= NOW() - INTERVAL '30 days'
GROUP BY day
ORDER BY day DESC;
