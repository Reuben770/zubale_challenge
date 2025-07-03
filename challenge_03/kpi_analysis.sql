-- KP1 - The date with max amount of orders

SELECT 	created_date as order_created_date,
		sum(quantity) as total_quantity,
        sum(quantity*price) as total_price_usd,
        count(ord.id) as order_count
FROM orders ord
inner join products prd on ord.product_id = prd.id
group by created_date
order by order_count desc
limit 1;


-- KP2 - The most demanded product
SELECT 	name as product_name,
		sum(quantity) as total_quantity,
        sum(quantity*price) as total_price_usd,
        count(ord.id) as order_count
FROM orders ord
inner join products prd on ord.product_id = prd.id
group by product_name
order by total_quantity desc
limit 1;


-- KP3 - The top 3 most demanded categories

SELECT 	category ,
		sum(quantity) as total_quantity,
        sum(quantity*price) as total_price_usd,
        count(ord.id) as order_count
FROM orders ord
inner join products prd on ord.product_id = prd.id
group by category
order by total_quantity desc
limit 3;