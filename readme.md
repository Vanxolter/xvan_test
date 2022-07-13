
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

![result 1](https://github.com/Vanxolter/xvan_test/blob/c28bf4ff71e916f551e332092421290e95a7cee7/results/%D0%BA%D1%83.jpg)  

2) Решение:  

