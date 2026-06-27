-- Write your query below


select * from seller s
    join orders o on s.seller_id = o.seller_id
    where s.seller_id not in (
        select seller_id from orders
            where sale_date between '2020-01-01' and '2020-12-31'
    )
    order by s.seller_name;