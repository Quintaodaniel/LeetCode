SELECT W.id FROM Weather w
JOIN Weather t
    ON w.recordDate = DATE_ADD(t.recordDate, INTERVAL 1 DAY)
    WHERE w.temperature > t.temperature