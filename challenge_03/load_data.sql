-- La ruta al archivo new_products.csv

TRUNCATE TABLE products;
\copy products (id,name,category,price) FROM '/root/postulaciones/zubale/data/products.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER TRUE);

TRUNCATE TABLE orders;
\copy orders (id,product_id,quantity,created_date) FROM '/root/postulaciones/zubale/data/orders.csv' WITH (FORMAT CSV, DELIMITER ',',HEADER TRUE);

-- Después de ejecutar \copy, los nuevos productos tendrán IDs generados automáticamente.