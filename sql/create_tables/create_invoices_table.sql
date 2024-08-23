CREATE TABLE IF NOT EXISTS account_invoice (
    id SERIAL PRIMARY KEY,
    number VARCHAR(255),
    date_invoice DATE,
    amount_total NUMERIC
);
