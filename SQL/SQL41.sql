"""
思路如下：
1.利用ROW_NUMBER 对每个user_id登录时长进行升序排序，得到date_order列
2.利用DATE_SUB 将fdate与date_order相减，得到伪日期列-date2，若连续登录，date2应相同
3.COUNT计算连续登陆时长 取 MAX
"""

SELECT 
    DISTINCT user_id, 
    MAX(consec_day) AS max_consec_days
FROM(
    SELECT 
        user_id, 
        date2,
        COUNT(date2) AS consec_day
    FROM(
        SELECT 
            *,
            DATE_SUB(fdate, INTERVAL date_order day) AS date2 -- 日期减去特定天数
        FROM(
            SELECT DISTINCT
                *,
                ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY fdate) AS date_order
            FROM tb_dau
            WHERE fdate BETWEEN '2023-01-01' AND '2023-01-31'
            ) AS t
        ) AS t2
    GROUP BY user_id, date2
    ) AS t3
GROUP BY user_id;
