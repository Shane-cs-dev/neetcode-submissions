-- Write your query below

select orders.customer_id, customers.customer_name from orders
    join customers on customers.customer_id = orders.customer_id
    group by orders.customer_id, customers.customer_name
    having sum(case when product_name = 'A' then 1 else 0 end) > 0 
    and sum(case when product_name = 'B' then 1 else 0 end) > 0 
    and sum(case when product_name = 'C' then 1 else 0 end) = 0
    order by customers.customer_name;
