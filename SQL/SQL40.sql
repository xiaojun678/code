with t as (
    select 
        month(fdate) as month,
        row_number() over (partition by 
                            month(fdate) 
                            order by 
                                count(*) desc,
                                song_id) -- 播放次数相同时按照id排序
        as ranking,
        song_name,
        count(*) as play_pv
    from play_log
    left join user_info using(user_id)
    left join song_info using(song_id)
    where 
        year(fdate) = '2022'
        and age between 18 and 25
        and singer_name = '周杰伦'
    group by month(fdate),
            song_name,
            -- 因为窗口函数中用到song_id排序 所以分组时要加上song_id
            song_id
)

select *
from t
where 
    ranking <= 3


