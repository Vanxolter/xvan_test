    SELECT bid.client_number, COUNT(event_value.outcome) AS Wins, COUNT(bid.client_number) AS Loses
    FROM bid
    JOIN event_value ON bid.play_id = event_value.play_id
    WHERE outc
    GROUP BY bid.client_number
    LIMIT 10;