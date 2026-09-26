/* Write your T-SQL query statement below */
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT
        id,
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev_num,
        LAG(num, 2) OVER (ORDER BY id) AS prev_prev_num
    FROM Logs
) AS t
WHERE num = prev_num
  AND num = prev_prev_num;