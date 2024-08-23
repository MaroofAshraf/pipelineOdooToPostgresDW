import pandas as pd
from odoorpc import ODOO

def extract_invoices():
    odoo = ODOO('your_odoo_host', port=8069)
    odoo.login('your_db', 'user', 'password')
    invoices = odoo.env['account.invoice'].search_read([], ['number', 'date_invoice', 'amount_total'])
    invoices_df = pd.DataFrame(invoices)
    return invoices_df
