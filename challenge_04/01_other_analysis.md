
**Insight 1**: Identification of Products and Categories with Highest Revenue

1. **Why it's valuable**: This allows the company to identify which products and product categories generate most of their income (revenue). This is fundamental for strategic decision-making in areas such as:
    - **Inventory Management**: Ensuring sufficient stock of the most profitable products.
    - **Marketing and Sales**: Focusing promotional efforts on high-value products and categories.
    - **Pricing and Promotions**: Analyzing if low-unit-price but high-volume products contribute significantly, or if expensive items are driving revenue.
    - **Product Development**: Understanding which types of products (categories) resonate most with customers.

2. **How to get it**:

    - **SQL Query**:
    ```sql 
            -- Products by Total Revenue 
            SELECT  p.id AS product_id,
                    p.name AS product_name,
                    p.category,
                    SUM(o.quantity * p.price) AS total_revenue  t
            FROM orders o
            INNER JOIN products p ON o.product_id = p.id
            GROUP BY p.id, p.name, p.category  
            ORDER BY total_revenue DESC  
            LIMIT 10; 

              -- Category by Total Revenue 

            SELECT  p.category,
                    SUM(o.quantity * p.price) AS total_revenue  t
            FROM orders o
            INNER JOIN products p ON o.product_id = p.id
            GROUP BY p.category  
            ORDER BY total_revenue DESC  
            LIMIT 10; 
    

**Insight 2**: Analysis of Sales Volume and Frequency by Product/Category
1. **Why it's valuable**: Revenue is not the only performance indicator. A product might generate high revenue because it's very expensive but sells few units. Another might generate less unit revenue but sell a huge volume or appear in many more orders.
    - **Volume (quantity)**: Indicates popularity in terms of units moved. Important for logistics, production, and demand forecasting.
    - **Frequency (order_count)**: Indicates how many different times (in how many orders) a product or category has been purchased. A product with high frequency but low average quantity per order might be a "complementary" or "impulse" item. A product with low frequency but high average quantity might be a "bulk" purchase or a large item.
    - Combining these metrics (volume, frequency, revenue) provides a more complete picture than revenue alone.

2. **How to get it**:

    - **SQL Query**:
    ```sql
            -- Products by Volumen and Frecuenciay 
            SELECT  p.id AS product_id,
                    p.name AS product_name,
                    p.category,
                    SUM(o.quantity) AS total_quantity_sold,  
                    COUNT(o.id) AS order_count,  
                    SUM(o.quantity * p.price) AS total_revenue  
            FROM orders o
            INNER JOIN products p ON o.product_id = p.id
            GROUP BY p.id, p.name, p.category
            ORDER BY total_quantity_sold DESC  
            LIMIT 10;    

              -- Category by Volumen and Frecuency

            SELECT   p.category,
                    SUM(o.quantity) AS total_quantity_sold,  
                    COUNT(o.id) AS order_count,  
                    SUM(o.quantity * p.price) AS total_revenue  
            FROM orders o
            INNER JOIN products p ON o.product_id = p.id
            GROUP BY p.category
            ORDER BY total_quantity_sold DESC  
            LIMIT 10; 

**Insight 3**: Analysis of Sales Trends Over Time
1. **Why it's valuable**: This allows identifying seasonal patterns, sales spikes (perhaps related to promotions or events), growth or decline over time. It's crucial for demand planning, marketing campaigns, resource allocation, and evaluating historical performance.
2. **How to get it**:  
    
    - **SQL Query**:
    ```sql

            --- Daily Total Revenue and Quantity

            SELECT
                o.created_date, 
                SUM(o.quantity) AS daily_quantity,
                SUM(o.quantity * p.price) AS daily_revenue
            FROM orders o
            INNER JOIN products p ON o.product_id = p.id
            GROUP BY o.created_date
            ORDER BY o.created_date ASC;  

            --- Weekly Total Revenue and Quantity, if we have another table for days,weeks, quarter, it's possible to generate other analisys by this frecuency.

            SELECT
                DATE_TRUNC('week', o.created_date)::DATE AS week_start_date, 
                SUM(o.quantity) AS weekly_quantity,
                SUM(o.quantity * p.price) AS weekly_revenue
            FROM orders o
            INNER JOIN products p ON o.product_id = p.id
            GROUP BY DATE_TRUNC('week', o.created_date)
            ORDER BY week_start_date ASC;

**These three areas (revenue performance, volume/frequency performance, and temporal performance) provide a solid foundation for understanding sales and product behavior, allowing informed decisions to optimize operations and business strategies.**
