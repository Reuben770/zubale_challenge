CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,  -- Asumiendo que product_id no puede ser nulo
    quantity INTEGER NOT NULL,    -- Asumiendo que quantity no puede ser nulo
    created_date DATE NOT NULL    -- Usamos DATE para el formato 'YYYY-MM-DD'. Asumiendo no nulo.
);

-- Creación de índices para optimizar consultas
CREATE INDEX  IF NOT EXISTS idx_orders_product_id ON orders (product_id);

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);