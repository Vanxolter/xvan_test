
Тестовое Django
------------------------------
Деплой первого задания: https://iksvanlavrov.herokuapp.com/


Тестовое SQL
--------------------------------------


1) Решение:

SELECT bid.client_number, 
SUM(CASE WHEN event_value.outcome = 'win' THEN 1 end) AS Побед, 
SUM(CASE WHEN event_value.outcome = 'lose' THEN 1 end) AS Поражений  
FROM bid JOIN event_value ON bid.play_id = event_value.play_id 
GROUP BY bid.client_number LIMIT 10;

Результат:

+---------------+------------+--------------------+
| client_number | Побед      | Поражений          |
+---------------+------------+--------------------+
|             1 |         46 |                 92 |
|             2 |         45 |                 90 |
|             3 |         45 |                 90 |
|             4 |         43 |                 86 |
|             5 |         45 |                 90 |
|             6 |         45 |                 90 |
|             7 |         44 |                 88 |
|             8 |         45 |                 90 |
|             9 |         45 |                 90 |
|            10 |         45 |                 90 |
+---------------+------------+--------------------+
10 rows in set (0,06 sec)


2) Решение:

