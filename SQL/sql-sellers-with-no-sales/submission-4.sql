-- Write your query below


select s.seller_name from seller s
    left join orders o on s.seller_id = o.seller_id
    where s.seller_id not in (
        select seller_id from orders
            where sale_date between '2020-01-01' and '2020-12-31'
    )
    group by s.seller_id, s.seller_name
    order by s.seller_name;