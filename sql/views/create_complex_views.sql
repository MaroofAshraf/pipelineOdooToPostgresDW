-- Complex view using CTE, subqueries, and window functions
CREATE VIEW customer_invoice_summary AS
WITH recent_invoices AS (
    SELECT
        id,
        number,
        date_invoice,
        amount_total,
        ROW_NUMBER() OVER(PARTITION BY res_partner.id ORDER BY date_invoice DESC) AS rn
    FROM
        account_invoice
    JOIN
        res_partner ON res_partner.id = account_invoice.partner_id
)
SELECT
    res_partner.name,
    res_partner.email,
    res_partner.phone,
    recent_invoices.number AS last_invoice_number,
    recent_invoices.date_invoice AS last_invoice_date,
    recent_invoices.amount_total AS last_invoice_amount
FROM
    res_partner
LEFT JOIN
    recent_invoices ON res_partner.id = recent_invoices.partner_id
WHERE
    recent_invoices.rn = 1;
