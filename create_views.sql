
CREATE VIEW error_total AS
    (SELECT DATE(time) AS date, COUNT(*) AS num
    FROM log
    WHERE status = '404 NOT FOUND'
    GROUP BY date
    ORDER BY date);

CREATE VIEW total AS
    (SELECT DATE(time) AS date, COUNT(*) AS num
    FROM log
    GROUP BY date
    ORDER BY date);
